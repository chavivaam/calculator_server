from functools import lru_cache
import exceptions


def add(x, y):
    """Add Function"""
    return "{}+{}={}".format(x, y, x + y)


def subtract(x, y):
    """Subtract Function"""
    return "{}-{}={}".format(x, y, x - y)


def multiply(x, y):
    """Multiply Function"""
    return "{}*{}={}".format(x, y, x * y)


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise exceptions.ZeroDevision()
    
    return "{}/{}={}".format(x, y, str(x / y).rstrip(".0"))
#===============================================================

@lru_cache(maxsize=None)
def calculate_exp(operand_l, operand_r, operator):
    op_functions = {"plus": add, "minus": subtract, "multiply": multiply, "divide": divide}
    
    op_function = op_functions.get(operator, None)

    if(not op_function):
        raise exceptions.InvalidOperand()

    return op_function(operand_l, operand_r)  
        
