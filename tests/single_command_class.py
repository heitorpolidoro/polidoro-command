from pcommand import command


class SingleCommandClass:
    @staticmethod
    @command
    def singlecmd():
        return "singlecmd"

    @staticmethod
    def ignoredcmd():
        return "ignoredcmd"
