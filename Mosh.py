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
