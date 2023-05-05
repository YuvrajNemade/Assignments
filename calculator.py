#for addition
def add(num1, nun2):
    return num1 + num2

#for subtraction
def sub(num1, num2):
    return num1 - num2

#for multiply
def multiply(num1, num2):
    return num1 * num2

#for divide
def divide(num1, num2):
    return(num1 / num2)


num1 = float(input("enter firt number: "))
num2 = float(input("enter second number: "))
print("Select operations.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while(True):
#Take get user input
 choice = int(input("Enter choice"))
 if choice == 1:
    print(add(num1,num2))

 elif choice == 2:
    print(sub(num1,num2))

 elif choice == 3:
    print(multiply(num1,num2))

 elif choice == 4:
    print(divide(num1,num2))