#Comments in python
print("Hello World!") #We do not need the ;

#Create variables
name = "Fernanda"
last_name = 'Murillo' #We can use double or single quotes. Both are valid stringes. 
age = 30
total = 12.34
found = False 

print("My name is", name, last_name, "I am", age, "years old.",  "These are some other values:", total, "and", found)

#We are going to use camelCase 

#Concatenate strings
print(name + " " + last_name)

#Maths
print(3 + 9) 
print(3 - 9)
print(3 * 9)
print(3 / 9)

#Error
#print("name" + 3)

#Conditional statements
if(age < 100): #Every code block starts with : and indentation
    print("yes")
    #print("Inside the if")
elif(age == 100): #In python parentheses
    print("Congratulations, ypu got to live a century")
else:
    print("Sorry, you are getting old")

print("Outside the if") #Indentation

#AND and OR are just and or

#Creating a function in Python
def say_hello():
    print("Hello there")
    print("from a function")

#Call the function
say_hello()

#A function receiving a parameter
def say_hi(name): #A function can receive as manu parameters as we need
    print("Hi " + name)

#Calling the function
say_hi("María")
say_hi(name)

#A function can return a value
def get_day():
    return "Monday 13th 2023"

#Calling the function
day = get_day()
print(day)