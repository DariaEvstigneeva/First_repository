def hello2(x):
    print('Hello, ' + x + '!')

hello2('world')
hello2('daria')
hello2('maria')

def hello():
    return 'Hello,world'

print (hello())
print (hello())


def percents2(x, y):
    one_percent = x / 100
    result = y / one_percent
    print(str(y) + " это " + str(result) + " % из " + str(x))

percents2(200,50)

def percents(x, y):
    one_percent = x/100
    result = y / one_percent
    return result


def print_percents(x, y):
    print(str(y) + " это " + str(percents(x, y)) + " % из " + str(x))


print_percents(200,50)

#для классов и объектов

from math import sqrt

def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return sqrt(dx*dx+dy*dy)

print(distance(0,0,3,4))

#классы и объекты

from package_for_learn_function.classy import *

a=Point(0, 0)
b=Point(3, 4)
print (a.distance2(b))
print (a==b)
print (a==a)


# сортировка списков по координате y

l1 = [Point(0,0), Point(1,2), Point(2,1)]
l2 = sorted(l1)
print("ok")


# тест else if
from math import sqrt

def solve(a, b, c):
    d = b*b - 4*a*c
    if d<0:
        print ("Нет решений")
    else:
        if d==0:
            x= -b / (2*a)
            print ("Одно рещение " + str(x))
        else:
            x1 = (-b + sqrt(d)) / (2*a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print("Два решения " + str(x1) + " и " + str(x2))



solve(1, 2, 1)
solve(1, 5, 6)
solve(1, 1, 1)


# тест elif
from math import sqrt

def solve(a, b, c):
    d = b*b - 4*a*c
    if d<0:
        print ("Нет решений")
    elif d==0:  # условие elif может повторятся многое колво раз
        x= -b / (2*a)
        print ("Одно рещение " + str(x))
    elif d>0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("Два решения " + str(x1) + " и " + str(x2))
    else:  # условие всегда должно кончаться else
        print("Ошибка")



solve(1, 2, 1)
solve(1, 5, 6)
solve(1, 1, 1)


i1 = [Point (2, 1), Point(0,0), Point(1,2)]

i2 = sorted(i1)
print(i1)
print(i2)


i1 = [Point (2, 1), Point(0,0), Point(1,2)]

def x(p): # ф-ция, которая в качестве параметра принимает объект типа поинт и возвращает координату х
    return p.x

i2 = sorted(i1, key=x) # при вызове ф-ции сортед, нужно указать доп.параметр

print(i1)
print(i2)

def y(p):
    return p.y

i2 = sorted(i1, key=y) # при вызове ф-ции сортед, нужно указать доп.параметр

print(i1)
print(i2)

i1 = [Point (2, 1), Point(0,0), Point(1,2)]

i2 = sorted(i1, key=lambda p: p.y) # конструкция лямбда определеяет анонимную функцию, где p входной параметр, в p.y результат

print(i1)
print(i2)

i1 = [Point (3, 1), Point(0,3), Point(1,2)]

i2 = sorted(i1, key=lambda p: p.distance2(Point (0,0))) # конструкция лямбда определеяет анонимную функцию, где p входной параметр, в p.y результат

print(i1)
print(i2)

# 4 занятие, видео 17 - конструкция for для циклов

d=[]

for i in range (-5, 6):
    d.append(Point(i, i*i))

print (d)

d=[]

for i in range (-5, 6):
    d.append(Point(i, i*i))

for el in d: # чтобы элемент списка печатался на отдельной строке
    print (el)


d=[]

for i in range (-5, 6):
    d.append(Point(i, i*i))

for el in d: # поменяем координату y на противоположную (т.е разверем параболу вверх ногами)
    el.y = -el.y

print (d) # исходный список разрушается, т.е меняются элмеметы которые в нем хранились

# чтобы не разрушался старый список

d=[]

for i in range (-5, 6):
    d.append(Point(i, i*i))

d2=[]

for el in d:
     d2.append(Point(el.x, -el.y))

print (d)
print (d2)

# укороченная запись, которая позволяет избавиться от циклов for -  list comrehension
d=[Point(i, i*i) for i in range (-5, 6)]

d2=[Point(el.x, -el.y) for el in d]

print (d)
print (d2)