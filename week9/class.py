#class Person:
    #def __init__(self, name):
        #self.name = name
        #print("I am calling")
    
    #def eat(self):
        #print(f"{self.name} is eating")

    #def sleep(self):
        #print(f"{self.name} is sleeping")

#obj = Person("John")
#obj.eat()

#obj2 = Person("Sarah")
#obj2.eat()

#class person:
    #def play(self):
        #print("John is playing")

    #def play(self):
        #print("Sarah is playing")

#obj = person()
#obj.play()


#class person:
    #def study(self):
        #print("John is playing")

    #def study(self):
        #print("Sarah is playing")

#obj = person()
#obj.study("John")

#class Person:
    #def __init__(self):
        #print("I am calling")

#obj1 = Person()
#obj2 = Person()
#obj3 = Person()

#Class Inheratence
class Parent:

    def sayHi(self):
        print("Hi from parent class")

class child(Parent):
    def greet(self):
        print("Hi from child class")

pa = Parent()
pa.sayHi()

ch = child()
ch.greet()
ch.sayHi()