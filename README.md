
## 01. First program 

```Python
## 01. FIrst Program

print ("Hello World!")
print ("Zizan")
```



## 02. How codes in python get executed?

1. Python reads code line by line.
2. Interpreter works here. It helpes computer to read the codes we want to execute by their program.




## 00. Some keywords

```Keywords
1. IDE = Integrated Development Environemnt
2. GUI = Graphical User Interface
3. Interpreter = An interpreter is a program that reads and executes Python code.
It is responsible for translating and executing each line of Python code in real-time.
```



## 03. Data types

### 03.01. Number types 


```Python
## Number types 

# decimal
a_decimal = 11
print(a_decimal)

# hexadecimal 
print(hex(a_decimal)) #0xb

#octal
print(oct(a_decimal))

#float
a_float = 1.22
print(a_float)
```


Output: 

```result
11
0xb
0o13
1.22
```

### 03.02. String and Boolean


```Python
name = 'Zizan'
is_published = True
print(name,is_published)
```


Output: 
```Output
Zizan True
```


### 03.03. Exercise

A patient named John Smith (He is a new patient), 20 years old. Express this statement with variables.


```Python
name = 'John Smith'
age = 20
new_patient = True


print(f"The patient's name is {name}, aged {age}")

if new_patient == True:
    print(f"{name} is a new patient")
```


Output:

```Output
The patient's name is John Smith, aged 20
John Smith is a new patient
```



## 04. Getting Input

```Python
name = input("What's your name?:")
print(f"Hi {name}")
```


Output:

```Output
What's your name?:Zizan
Hi Zizan
```



### 04.01. Exercise

Get input: name and favorite color.
Print: For example, john likes red.


```Python
name = input("What's your name?: ")
fav_color = input("What's your favorite color?: ")
print(f"{name} likes {fav_color}")
```


Output:

```Output
What's your name?: Zizan
What's your favorite color?: Red
Zizan likes Red
```
