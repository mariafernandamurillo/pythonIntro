#Imports

#Global vars

#Funtions 
def print_menu():
    separator = "-----------------------"

    print(separator)
    print(" Calc 3000")
    print(separator)
    print("[1] Sum two numbers")
    print("[2] Substract two numbers")
    print("[3] Multiply two numbers")
    print("[4] Division two numbers")



#Plain instructions
print_menu()
opt = input("Please select an option: ")
num1 = float(input("Please, write number 1: "))
num2 = float(input("Please, write number 2: "))

if opt == "1":
    #Ask for num1, num2, and print the result of adding those numbers
    result = num1 + num2
    print("Result is: " + str(result))

elif opt == "2":
    result = num1 - num2
    print("Result is: " + str(result))
    

elif opt == "3":
    result = num1 * num2
    print("Result is: " + str(result))

elif opt == "4":
    if(num2 == 0):
        print("Zero is not allowed for the division")
    else:
        result = num1 / num2
        print("Result is: " + str(result))

else:
    print("That's not an option, my friend.")

