def greet(fname, lname, age):
    print ('Hello World')
    print(fname + ' ' + lname + ' ' + age)

greet(fname="doan", lname="huy", age="18")

x = lambda a, b : a * b
print(x(5, 10))

def myfunc(n):
    return lambda a : a * n 


mydoubler = myfunc(2)

print(mydoubler(11))

class ToanHoc:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


p1 = ToanHoc("Huy", 18)

print(p1.name)
print(p1.age)

import platform
x=dir(platform)
print(x)

import datetime
x = datetime.datetime.now()
print(x.strftime('%B'))

import math 
x = math.sqrt(16)
print(x)

import json

x = '{"name": "Huy", "age": 19, "city": "Ha Noi"}'

y = json.loads(x)

print(y['name'])