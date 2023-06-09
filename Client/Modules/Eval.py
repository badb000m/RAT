class Eval:
    """
    Evaluation. Allows you to execute custom Python code on command.
    You may import packages too (They have to be Python installed.)
    """
    def __init__(self, args: list):
        self.args = args
        self.to_execute: str = '\n'.join(self.args)

        print(self.to_execute)

        try:
            exec(self.to_execute)
        except Exception as err:
            print(err)
