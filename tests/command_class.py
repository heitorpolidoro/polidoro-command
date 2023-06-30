from pcommand import command


@command
class CommandClass:
    attr = "attr"

    @staticmethod
    def cmd1():
        return "cmd1"

    @staticmethod
    def cmd2():
        return "cmd2"

    def _ignored(self):
        pass

    @classmethod
    def _ignored_class(cls):
        pass

    @staticmethod
    def _ignored_static():
        pass


