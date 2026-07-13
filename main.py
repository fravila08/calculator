class Calculator:

    def add(self, arg_1:int, arg_2:int)->int:
        self.check_type(arg_1, arg_2)
        return arg_1 + arg_2
    
    def multiply(self, arg_1:int, arg_2:int)-> int:
        self.check_type(arg_1, arg_2)
        return arg_1 * arg_2
    
    @classmethod
    def check_type(cls, arg_1, arg_2) -> bool | ValueError:
        if not isinstance(arg_1, int) or not isinstance(arg_2, int):
            raise ValueError("Both arguments must be an integer")
        return True
