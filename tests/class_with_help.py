from polidoro_command import command


class CMD:
    help = "Class Help"

    @staticmethod
    @command
    def command_test():
        return "command in class"
