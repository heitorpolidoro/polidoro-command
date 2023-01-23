from collections import defaultdict

import pytest

from polidoro_command import PolidoroArgumentParser, command


@pytest.fixture
def parser():
    PolidoroArgumentParser.commands = defaultdict(list)
    PolidoroArgumentParser._subparsers_dict = {}
    return PolidoroArgumentParser(prog="testCommand")


@pytest.fixture
def command_no_arguments():
    @command
    def command_test():
        return "command called"


@pytest.fixture
def command_with_arguments():
    @command
    def command_test(po, /, pwod, pwd='default_pwd', *args, ko='default_ko', _ko_ignored=None, **kwargs):
        return f"command called with {po}, {pwod}, {pwd}, {ko}, {args}, {kwargs}"


@pytest.fixture
def command_in_class():
    class CMD:
        @staticmethod
        @command
        def command_test():
            return "command in class"


def assert_call(parser, commands, expected_output, capsys, exit_code=0, expected_exception=SystemExit):
    except_info = None

    if expected_exception:
        with pytest.raises(expected_exception) as except_info:
            parser.parse_args(commands.split())
        if expected_exception == SystemExit:
            assert (
                    except_info.value.code == exit_code
            ), f"\nExpected code: {exit_code}\nExit code:{except_info.value.code}"
    else:
        parser.parse_args(commands.split())

    output, error = capsys.readouterr()
    if expected_exception and exit_code:
        output += error
    if not output and except_info:
        output = str(except_info.value)

    assert output == expected_output
