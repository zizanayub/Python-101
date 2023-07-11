## 01. FIrst Program

print ("Hello World!")
print ("Zizan")




## 03. Variables


## 03.01. Basic Syntax 

price = 10
print (price)

## 03.02. Updatation

price = 10 
price = 20 
print (price)


## 03.03. Data types

price = 10
rating = 4.9 
name = "Zizan"
is_published = True
print(price, rating, name, is_published)


## 03.04. Exercise
## Check a patient named John Smith, 20 years age and he's a new patient.

name = "John Smith"
age = 20
new_patient = True 
print(name, age, new_patient)








# 04. Getting inputs 
name = input("What is your name?: ")
favorite_color = input('What is your favorite color?: ')
print(name + ' likes ' + favorite_color)









# 05. Type conversion
birth_year = input("birth year: ")
age = 2023-int(birth_year)
print(age)


# 05.01. Identifying types 
birth_year = input("birth_year: ")
print(type(birth_year))
age = 2023-int(birth_year)
print(type(age))


# 05.02. Identifying types (with conversion)
birth_year = int(input("birth_year: "))
print(type(birth_year))
age = 2023-int(birth_year)
print(type(age))






# 06. Python Strings 
course = 'Python for "beginners"'
print(course)



# 06.01. Indexing.
print(course[0])   #Will give output of first character.
print(course[-1])  #Will give output of last character. 



#06.02. Indexing (Staring:Ending)
print(course[0:3]) #Pyt
print(course[2:]) #thon......
print(course[:5]) #Pytho



#06.03. Exercise
name = 'jeniffer'
print(name[1:-1])




# 07. Formatted Strings

# 07.01. How we do concatenation normally
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder!'
print(message)


# 07.02. How we can do with 'Formatted String'
first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a coder'
print(message)





# 08. String Methods
course = 'Python for Beginners'
print(len(course))  #Length Function

# Upper and Lower Methods
print(course.upper()) #Converts to upper
print(course.lower()) #Converts to lower 

# Find Method
print(course.find('P'))
print(course.find('Beginners'))

#Replace Method
print(course.replace('Beginners','Absolute Beginners'))

#IN Operator
print('Python' in course)







# 09. Arithmetic Operators
print(10/3)
print(10//3) #Division, but it will output int only
print(10%3)
print(10**3) #Exponent


# 09.01. Augmented Arithmetic Operator
x = 10
x += 2
print(x)





# 10. Operator Precendence
# Exercise
x = (2+3)*10-3
print(x)




# 11. Math Functions
x = 2.9
print(round(x))
x = -2.9
print(abs(x))



# 11.01. Math module
import math 
print(math.ceil(2.9))
print(math.floor(2.9))



# 12. IF Statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm cloths.")
else:
    print("It's a lovely day!")
print("Enjoy your day!")




# 12.01. Exercise
price = 1000000
has_good_credit = True


if has_good_credit:
    down_payment = price*0.1
else:
    down_payment = price*0.2

print(f"down payment: {down_payment}") 










# 12. IF Statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm cloths.")
else:
    print("It's a lovely day!")
print("Enjoy your day!")




# 12.01. Exercise
price = 1000000
has_good_credit = True


if has_good_credit:
    down_payment = price*0.1
else:
    down_payment = price*0.2

print(f"down payment: {down_payment}") 




# 13. Logical operators (AND, OR, NOT)

# 13.01. and operator
has_good_income = True 
good_credit_score = True

if has_good_income and good_credit_score:
    print("Eligible for loan!")
else:
    print("Not eligible for loan!")
print("Thank you!")



# 13.02. or operator
has_good_income = True
has_criminal_record = False


if has_good_income or has_criminal_record:
    print("Eligible for loan!")
else:
    print("Not eligible for loan!")



# 13.03. not operator
has_good_income = True 
has_criminal_record = False 
good_credit_score = True


if has_good_income and not has_criminal_record and good_credit_score:
    print("Eligible for loan!")
else:
    print("Not eligible for loan!")





# 14. Comparison operator
temperature = int(input("Enter the temperature: "))

if temperature > 30 and temperature < 40:
    print(f"Because of higher than {temperature} temperature, it's a hot day!")
elif temperature < 10:
    print(f"Because of less than {temperature} temperature, it's cold day!")
elif temperature == 40:
    print("It's too high temperature today! Stay safe!")
else:
    print("Just a normal day!")



# 14.01. Exercise
name = input("What's your name: ")

if len(name) < 3:
    print("Name must be 3 characters long!")
elif len(name) > 50:
    print("Name must be 50 characters long!")
else:
    print("Name is Ok!")







# 15. Project: Weight converter
weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight*0.45
    print(f"You are {converted} kg")
elif unit.upper() == "K":
    converted = weight/0.45
    print(f"You are {converted} pounds")







# 16. While loops
i = 0
while i <= 5:
    print(i)
    i += 1
print("Done")



# 16.01. print stars by while loop
i = 0
while i < 5:
    print('*' * i)
    i += 1
print("Done")








# 17. Building a guessing game
secret_number = 10
guessing_count = 0
guessing_limit = 3

while guessing_count < guessing_limit:
    guess_number = int(input("Guess the number: "))
    guessing_count += 1
    if guess_number == secret_number:
        print(f"You won! The secret number is {secret_number}")
        break
else:
    print(f"You failed! You tried all {guessing_count} attempts!")







# 18. Car game
command = True
while command:
    command= input("> ").lower()
    if command == "start":
        print("Car started!")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
start - to start,
stop - to stop,
quit - to quit the operations""")
    elif command == "quit":
        print("Ok!Thanks!")
        break
    else:
        print("Sorry! I didn't understand!")




# 18.01. Car game (Make it to the advanced level)


# Need to understand 


command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started!") 
        
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped!")









# 19. For loops

# String
for item in "Python":
    print(item)


#List
for item in [1,2,3,5]:
    print(item)
for element in ['John','Mick','Nick']:
    print(element)


#Range
for item in range(10):
    print(item)
for item in range(5,10):
    print(item)
for item in range(5,10,2):
    print(item)



#19.01. Exercise
price = [10,20,30]
total = 0
for number in price:
    total += number 
print(total)








#20.Nested Loop
for i in range(4):
    for j in range(3):
        print(f"({i}, {j})")


# 20.01.Challenge
# Draw an F with list

numbers = [5,2,5,2,2]
for number in numbers:
    print('X'* number)


#With nested loop
numbers = [5,2,5,2,2]
for item in numbers:
    output=""
    for count in range(item):
        output+="X"
    print(output)









# 21.Lists
list = [1,2,3,4,5]
print(list[2])
print(list[-1])
print(list[:3])
print(list[1:4])
print(list[2:])
print(list[:])
list[2] = 40
print(list)
new_value = list[2]
print(new_value)    



# 21.Exercise: Find the largest number in a list
numbers = [2,3,1,4,10,6]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number 
print(max)








#22.2D lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0])
print(matrix[0][1])

#Modify
matrix[0][2] = 23
print(matrix)


#Print all elements in the nested loop
for row in matrix:
    for number in row:
        print(number)







# 23. List Methods

numbers = [2,3,1,5,6,0]


# Append
numbers.append(3)
print(numbers)


# Insert (Used to insert in a specific index)
numbers.insert(1,3)
print(numbers)


#Remove
numbers.remove(5)
print(numbers)


# Hop (Removing last item on the list)
numbers.pop()
print(numbers)



# Index (Outputs the index number of an element)
print(numbers.index(1))



# In operator 
print(5 in numbers)


# Sort (Ascending)
numbers.sort()
print(numbers)


# reverse
numbers.reverse()
print(numbers)



# Copy
numbers_duplicated = numbers.copy()
print(numbers)
numbers_duplicated.append(9)
print(numbers_duplicated)





# Exercise
# Write a program to remove duplicates in a list

numbers_list = [1,2,3,4,3,2,1]
unique = []

for number in numbers_list:
    if number not in unique:
        unique.append(number)
print(unique)









# 24. tuples


# Indexing
numbers = (1,2,3,4,7)
print(numbers[1])


# Count
print(numbers.count(7))







# 25.Unpacking


# With tuples
coordinates = (1,2,3,7)
x,y,z,a = coordinates
print(x,y,z)


# With list
coordinates = [23,12,32]
x,y,z = coordinates
print(x,y,z)







# 26.Dictinaries

customer = {
    "name": "Zizan",
    "age" : 24,
    "is_employed" : True
    }


print(customer)
print(customer["name"])



# Get function
print(customer.get("birthdate"))    #None

# New value addition using Get Function
print(customer.get("birthdate","31 Dec, 1998"))


# Update
customer["name"] = "Zizan Ayub"
customer["birthdate"] = "01 Jan 1999"
print(customer)




# 26.01. Exercise


# My solution
answer = ""
input_the_numbers = input()
list_of_outputs = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four'
}
for number in input_the_numbers:
    if number in list(list_of_outputs.keys()):    #Keys() method 
        answer+=list_of_outputs[number]+" "
    else:
        answer+="!"+" "
print(answer)



# Using get()
answer = ""
input_the_numbers = input()
list_of_outputs = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four'
}

for number in input_the_numbers:
    answer += list_of_outputs.get(number,"!")+" "  #Exceptional usage of get method 
print(answer)








# 27. Emoji Converter 
message = input("> ")
words = message.split(' ')
emojis = {
    ":)" : "Happy Emoji",
    ":(" : "Sad emoji"
}

answer = " "
for word in words:
    answer += emojis.get(word,word) + " "
print(answer)










# 28. Functions 
def greet_user():
    print("Hi There")


greet_user()
# 2 blank lines after function definition is required.






# 29.Parameters
def greet_user(firstname,lastname):
    print(f"Hi {firstname} {lastname}")

greet_user("Zizan","Ayub")







# 30. Keyword arguments

# 30.01. Why we use?

def greet_user(firstname,lastname):
    print(f"Hi {firstname} {lastname}")
    print("Welcome Abroad!")


greet_user("Zizan")

# ERROR: greet_user() missing 1 required positional argument: 'lastname'



# 30.02. Keyword Arguments

def greet_user(firstname,lastname):
    print(f"Hi {firstname} {lastname}!")
    print("Welcome Abroad!")


greet_user ("Zizan",lastname = "Ayub")
    






# 31. Return Statement



# Basic Syntex 
def square(number):
    return number * number 


result = square(3)
print(result)



# If there is no return statement

def square(number):
    print(number*number)

print(square(3))

# Explanation is in the readme file







# 32. Creating a reusable function

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : "Happy Emoji",
        ":(" : "Sad Emoji"
    }
    
    answer = " "
    for word in words:
        answer += emojis.get(word,word)+" "
    return answer


message = input("> ")
print(emoji_converter(message))







# 33. Exceptions



# Single exceptions
try:
    age = int(input("Age> " ))
    print(age)
except ValueError:
    print('Invalid Value')     #If the user inputs different data types expcept integer or wwhole number 





# We can use multiple exceptions

try:
    age = int(input("Age> "))
    income = 20000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("Invalid Value")








# 35. Classes

class Point:
    def draw(self):
        print("Draw")
    def move(self):
        print("Move")


point1 = Point()    # Object
point1.x = 19   #Attribute
point1.y = 20   #Attribute
print(point1.x)

#Methods
point1.draw()
point1.move()





# It will give error. Because no object named 'point2' has been created
print(point2.x)







# 36. Cnstructors

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y 
    

point1 = Point(10,20)
print(point1.x, point1.y)





# 36.01. Exercise
class Person:
    
    def __init__(self,name):
        self.name = name 


    def greet(self):
        print(f"Hi! This is {self.name}")



new_employee = Person("John Smith")
print(new_employee.name)
new_employee.greet()

