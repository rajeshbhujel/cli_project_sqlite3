'''
        SIMPLE CALCULATOR IN PYTHON
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
'''
print("Select an opertion to perform: ")
print("1 ADD")
print("2 Subract")
print("3 Multiply")
print("4 Division")

operation = input()

if operation == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    #validation
    if(num1.isnumeric() and num2.isnumeric()):
        sum = int(num1) + int(num2)
        print("The sum of 2 numbers is:"+str(sum))
    else: 
        print("Type a valid number!")

elif operation == "2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        sub = int(num1) - int(num2)
        print("The difference between 2 numbers is: "+str(sub))
    else:
        print("Type a valid number!")

elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        mul = int(num1) * int(num2)
        print("The multiplication of 2 values : "+str(mul))
    else:
        print("Type a valid number!") 


elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        div = int(num1) / int(num2)
        print("The division of 2 numbers is: "+str(div))
else:
    print("Please enter the valid operation")

