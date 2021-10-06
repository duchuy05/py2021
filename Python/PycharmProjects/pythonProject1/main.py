class Person:
    def __init__(self, name):
        self.name = name


    def stt1(self):
        print(f'Hi I am {self.name}')


nguoi1 = Person('Huy')
nguoi1.stt1()

nguoi2 = Person('Duc')
nguoi2.stt1()


class Person:
    def __init__(self, height):
        self.height = height


    def hihi(self):
        print(f'Toi cao {self.height} cm')


class Person1(Person):
    def vedep(self):
        print('Toi qua dep')

class Person2(Person):
    pass


stt3 = Person1('173')
stt3.hihi()
stt3.vedep()

numbers = [1223, 2124324, 324254765, 324423]
numbers.sort()
numbers.reverse()
print(numbers)
print(max(numbers))

so = (1,2,3)
print(so[1])

customer = {
    'Name': 'Huy',
    'Age': '18',
    'Married': 'No'
}
customer['Name'] = 'Duc'
print(customer['Name'])

phone = input('Phone number: ')
chuso = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
xuatra = ''
for kitu in phone:
    xuatra += chuso.get(kitu, '!') + ' '
print(xuatra)

try:
    age = int(input('Age: '))
    income = int(input('Income: '))
    risk = income / age
    print('Risk: ',risk)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid')

import sys
try:
    x = int(input('Nhap x '))
    y = int(input('Nhap y '))
except ValueError:
    print('Invalid')
    sys.exit(1)
try:
    result = x / y
    print(f"{x} / {y} ", {result})

except ZeroDivisionError:
    print('0 cannot be divided')
    sys.exit(1)


fruit = 'Banana'
print(len(fruit))

n = int(input('Nhap so nguyen duong n '))
x = 0
for i in range(n+1):
    x += i
print(x)