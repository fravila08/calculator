class Calculator:

    def add(self, arg_1:int, arg_2:int)->int:
        if not isinstance(arg_1, int) or not isinstance(arg_2, int):
            raise ValueError("Both arguments must be an integer")
        return arg_1 + arg_2
