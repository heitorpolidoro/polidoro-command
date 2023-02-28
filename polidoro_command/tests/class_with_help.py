from polidoro_command import command


class CMD:
    _command_help = "Class Help"

    @staticmethod
    @command
    def command_test():
        return "command in class"
