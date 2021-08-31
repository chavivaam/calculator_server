class ZeroDivision(Exception):

    def __init__(self):
        
        self.message = "Error! integer devision by zero is prohibited"
        self.status_code = 422 #Unprocessable Entity
        super(ZeroDivision, self).__init__(self.message, self.status_code)

class InvalidOperand(Exception):
    def __init__(self):
        
        self.message = "Error! The valid operands are: +, -, *, /"
        self.status_code = 400 #Incorrect Syntax
        super(InvalidOperand, self).__init__(self.message, self.status_code)