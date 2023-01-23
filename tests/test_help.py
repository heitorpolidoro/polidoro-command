from polidoro_command import command
from tests.conftest import assert_call


def test_help_no_arguments(parser, command_no_arguments, capsys):
    assert_call(parser, "--help",
                """usage: testCommand [-h] {command_test}

commands:
    command_test

optional arguments:
  -h, --help    show this help message and exit
""",
                capsys)

    assert_call(parser, "command_test --help",
                """usage: testCommand command_test [-h]

optional arguments:
  -h, --help  show this help message and exit
""",
                capsys)


def test_help_with_arguments(parser, command_with_arguments, capsys):
    assert_call(parser, "--help",
                """usage: testCommand [-h] {command_test}

commands:
    command_test

optional arguments:
  -h, --help    show this help message and exit
""",
                capsys)

    assert_call(parser, "command_test --help",
                """usage: testCommand command_test [-h] [--pwd PWD] [--ko KO]
                                [--kwargs KWARGS ...]
                                po pwod [pwd] [args ...]

positional arguments:
  po
  pwod
  pwd
  args

optional arguments:
  -h, --help            show this help message and exit
  --pwd PWD
  --ko KO
  --kwargs KWARGS
""", capsys)


def test_help_in_class(parser, command_in_class, capsys):
    assert_call(parser, "--help", """usage: testCommand [-h] {cmd}

commands:
    cmd

optional arguments:
  -h, --help    show this help message and exit
""", capsys)
    assert_call(parser, "cmd --help", """usage: testCommand cmd [-h] {command_test}

commands:
    command_test

optional arguments:
  -h, --help    show this help message and exit
""", capsys)
    assert_call(parser, "cmd command_test --help", """usage: testCommand cmd command_test [-h]

optional arguments:
  -h, --help  show this help message and exit
""", capsys)


def test_custom_help(parser, capsys):
    @command(help="Custom help", config={
        "po": {"help": "PO Help"},
        "pwod": {"help": "PWOD Help"},
        "pwd": {"help": "PWD Help"},
        "args": {"help": "ARGS Help"},
        "ko": {"help": "KO Help"},
        "kwargs": {"help": "KWARGS Help"},
    })
    def command_test(po, /, pwod, pwd='default_pwd', *args, ko='default_ko', _ko_ignored=None, **kwargs):
        return "command called"

    assert_call(parser, "--help",
                """usage: testCommand [-h] {command_test}

commands:
    command_test
                Custom help

optional arguments:
  -h, --help    show this help message and exit
""",
                capsys)

    assert_call(parser, "command_test --help",
                """usage: testCommand command_test [-h] [--pwd PWD] [--ko KO]
                                [--kwargs KWARGS ...]
                                po pwod [pwd] [args ...]

positional arguments:
  po                    PO Help
  pwod                  PWOD Help
  pwd                   PWD Help (default: default_pwd)
  args                  ARGS Help (default: [])

optional arguments:
  -h, --help            show this help message and exit
  --pwd PWD             PWD Help (default: default_pwd)
  --ko KO               KO Help (default: default_ko)
  --kwargs KWARGS                        KWARGS Help (default: {})
""", capsys)


def test_custom_help_in_class(parser, capsys):
    # noinspection PyUnresolvedReferences
    from tests.class_with_help import CMD
    assert_call(parser, "--help", """usage: testCommand [-h] {cmd}

commands:
    cmd         Class Help

optional arguments:
  -h, --help    show this help message and exit
""", capsys)
    assert_call(parser, "cmd --help", """usage: testCommand cmd [-h] {command_test}

commands:
    command_test

optional arguments:
  -h, --help    show this help message and exit
""", capsys)
