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
