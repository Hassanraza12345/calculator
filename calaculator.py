#Create a basic calculator that can perform
#basic arithmetic operations such as addition,
#subtraction, multiplication, and division.using
#functions


class calculator:
    def __init__(self,value1,value2):
        """
        Initialize the calculator object with two numerical values.

        Parameters:
            value1 (float): The first numerical value.
            value2 (float): The second numerical value.
        """
        self.val1=value1
        self.val2=value2
    def addition(self):
        """
        Adding first and second value
        """
        print(self.val1+self.val2)
    def Substraction(self):
        """
        substracting  second value from first
        """
        print(self.val1-self.val2)
    def Multiplication(self):
        """
        Multiply first and second value
        """
        print(self.val1*self.val2)
    def Division(self):
        """
        dividing first by second value but second value
        is not null or zero
        """
        if self.val2 != 0:
            print(self.val1 / self.val2)
        else:
            print("Cannot divide by zero.")

obj1=calculator(23,45)
obj1.addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()
        
