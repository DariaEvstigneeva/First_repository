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