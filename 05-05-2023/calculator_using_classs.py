"""Performing calculator using class"""
class Calculator():
    """Perform operation on numbers"""
    def __init__(self, user_num1, user_num2):
        self.num1 = user_num1
        self.num2 = user_num2


    def add(self):
        """Performing adition"""
        return self.num1 + self.num2


    def sub(self):
        """Performing Subtraction"""
        return self.num1 - self.num2


    def multiply(self):
        """Performing Multiply"""
        return self.num1 * self.num2


    def divide(self):
        """Performing Divide"""
        return self.num1 / self.num2


num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num_object = Calculator(num1, num2)

print("Select operations.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = int(input("Enter choice"))

if choice == 1:
    print(num_object.add())

elif choice == 2:
    print(num_object.sub())

elif choice == 3:
    print(num_object.multiply())

elif choice == 4:
    print(num_object.divide())
else:
    print("enter a valid option")
