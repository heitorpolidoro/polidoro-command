from argparse import ArgumentError

from conftest import assert_call


def test_run_failure_no_arguments(parser, command_no_arguments, capsys):
    assert_call(parser, "command_test a", """usage: testCommand [-h] {command_test}
testCommand: error: unrecognized arguments: a
""", capsys, exit_code=2)


def test_run_failure_with_arguments(parser, command_with_arguments, capsys):
    assert_call(parser, "command_test", "the following arguments are required: po", capsys, exit_code=2, expected_exception=ArgumentError)
