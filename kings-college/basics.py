# -*- coding: utf-8 -*-

print(type("lucien"))
# assigning a variable
x = 'lucien'
y = 24 # assigning value 24
print(age)
# a year has passed
age = age + 1 # re-assigning a value to age
print(age)
pi = 3.14
cities = ['london', 'paris']
phonebook = { "number": 826492742, 
             "second_number": 482742974 }
print(first_name)

email = input('What is your email?')
password = input('What is your password?')

first_number = input('what is the first value?')
second_number = input('what is the second value?')
print(type(int(first_number)))
print(type(int(second_number)))
sum = int(first_number) + int(second_number)
print(sum)

print(type(str(10)))

first_name = 'lucien'
last_name = 'george'
age = 24
# concatenation
#full_name = "Hi my name is" + " " + first_name + " " + last_name + " and I am " + str(age) + " years old "

# interpolation
full_name = f"Hi my name is {first_name} {last_name} and I am {age} years old"
print(full_name)


import datetime
today = datetime.date.fromisoformat('2019-12-25')
print(today.strftime('%A, %b %d'))
















































