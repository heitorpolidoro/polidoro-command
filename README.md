# PCommand
[![Tests](https://github.com/heitorpolidoro/polidoro-command/actions/workflows/push.yml/badge.svg)](https://github.com/heitorpolidoro/polidoro-command/actions/workflows/push.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/heitorpolidoro/polidoro-command)
[![Coverage Status](https://coveralls.io/repos/github/heitorpolidoro/polidoro-command/badge.svg?branch=master)](https://coveralls.io/github/heitorpolidoro/polidoro-command?branch=master)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_polidoro-command&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_polidoro-command)

[![Latest](https://img.shields.io/github/release/heitorpolidoro/polidoro-command.svg?label=latest)](https://github.com/heitorpolidoro/polidoro-command/releases/latest)
![GitHub Release Date](https://img.shields.io/github/release-date/heitorpolidoro/polidoro-command)

![PyPI - Downloads](https://img.shields.io/pypi/dm/polidoro-command?label=PyPi%20Downloads)

![GitHub](https://img.shields.io/github/license/heitorpolidoro/polidoro-command)

Package to simplify creating command line arguments for scripts in Python.

#### How to use

- Decorate the function (or class methods) you want to expose on the command line with `@command`.
- Create an `ArgumentParser`.
- Call `parser.parse_args()`.

All keyword arguments to `@command` mirror those of [`argparse.ArgumentParser.add_argument`](https://docs.python.org/3/library/argparse.html#the-add-argument-method) except for `action` and `nargs`, which are inferred from the function signature.

Basic command

```python
from pcommand import ArgumentParser, command

@command
def cool_command():
    print("this is a command")

# Parse CLI
ArgumentParser().parse_args()
# OR
parser = ArgumentParser()
parser.parse_args()
```
```bash
$ python foo.py --help
usage: foo.py [-h] {cool_command}

commands:
  cool_command

options:
  -h, --help  show this help message and exit

$ python foo.py cool_command
this is a command
```

With arguments (use `*` to mark keyword-only parameters)

```python
from pcommand import ArgumentParser, command

@command
def command_with_arg(arg1, *, arg2=None):  # use * to separate positional from keyword-only arguments
    print(f"this is the command arg1: {arg1}, arg2: {arg2}")

ArgumentParser().parse_args()
```
```bash
$ python foo.py command_with_arg --help
usage: foo.py command_with_arg [-h] [--arg2 ARG2] arg1

positional arguments:
  arg1

options:
  -h, --help  show this help message and exit
  --arg2 ARG2

$ python foo.py command_with_arg Hello
this is the command arg1: Hello, arg2: None

$ python foo.py command_with_arg Hello --arg2 World
this is the command arg1: Hello, arg2: World
```

Using a class

```python
from pcommand import ArgumentParser, command

class ClassCommand:
    @staticmethod
    @command
    def command_in_class(*, arg="Oi"):  # keyword-only via *
        print(f"command_in_class called. arg={arg}")

ArgumentParser().parse_args()
```
```bash
$ python foo.py classcommand command_in_class
command_in_class called. arg=Oi

$ python foo.py classcommand command_in_class --arg Ola
command_in_class called. arg=Ola
```

Adding help text for the command and its arguments

```python
from pcommand import ArgumentParser, command

@command(help="command help")
@command.help(arg1="Arg1 Help", arg2="Arg2 Help")
def command_with_arg(arg1, *, arg2=None):  # keyword-only via *
    print(f"this is the command arg1: {arg1}, arg2: {arg2}")

ArgumentParser().parse_args()
```
```bash
$ python foo.py command_with_arg --help
usage: foo.py command_with_arg [-h] [--arg2 ARG2] arg1

positional arguments:
  arg1         Arg1 Help

options:
  -h, --help   show this help message and exit
  --arg2 ARG2  Arg2 Help (default: None)
```

How the parameter kind is parsed to argument type

| Parameter Kind       | Argument type                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------|
| POSITIONAL_ONLY      | Positional argument (required, `nargs=1`)                                                       |
| VAR_POSITIONAL       | Positional argument (optional, `nargs="*"`, `default=[]`)                                      |
| KEYWORD_ONLY         | Optional argument (`--name`, required, `nargs=1`, default from signature)                       |
| VAR_KEYWORD          | Optional argument (`--kwargs`, optional, `nargs="*"`, `default={}`; extra `--key value` pairs) |

For more information about parameter kinds, see Python's docs: https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind
