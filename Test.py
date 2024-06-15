# import example
import numpy as np

test = "this is my python test"

print(test)
print(test.capitalize())
print(test.split())

def randomAge(a):
    return np.random.randint(a,100)

class Person:
    def __init__(x,name,age):
        x.name =  name
        x.age = age

    def getPersonDetails(y):
        print(y.name+" is "+y.age)

me = Person("Stoyan", str(randomAge(7)))
me.getPersonDetails()