from argparse import ArgumentError

from tests.conftest import assert_call


def test_run_success_no_arguments(parser, command_no_arguments, capsys):
    assert_call(parser, "", "usage: testCommand [-h] {command_test}\n", capsys)
    assert_call(parser, "command_test", "command called\n", capsys, expected_exception=None)


def test_run_success_with_arguments(parser, command_with_arguments, capsys):
    assert_call(parser, "", "usage: testCommand [-h] {command_test}\n", capsys)
    assert_call(parser, "command_test PO PWOD",
                "command called with PO, PWOD, default_pwd, default_ko, (), {}\n",
                capsys, expected_exception=None)
    assert_call(parser, "command_test PO PWOD PWD ARG1 ARG2 --ko=KO --kw1=KW1",
                "command called with PO, PWOD, PWD, KO, ('ARG1', 'ARG2'), {'kw1': 'KW1'}\n",
                capsys, expected_exception=None)


def test_run_in_class(parser, command_in_class, capsys):
    assert_call(parser, "cmd", "usage: testCommand [-h] {cmd}\n", capsys)
    assert_call(parser, "command_test", "argument {cmd}: invalid choice: 'command_test' (choose from 'cmd')", capsys,
                expected_exception=ArgumentError)
    assert_call(parser, "cmd command_test", "command in class\n", capsys, expected_exception=None)
