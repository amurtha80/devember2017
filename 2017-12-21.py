#2017-12-12 Goal
##Learn some Python
##Get through at least 3 lessons from the following Udemy course:
##Python for Beginners - LearnToProgram, Inc. (Alex Bowers)


#Lab Exercise 8 - Custom Functions
##Your task is to create a function that will return a string of the type of
##data that is passed to it.
##The data types must be processed and checked as:
##1:    Alphanumeric
##2:    Digit (this is a number without decimal places)
##3:    Boolean

##My Attempt - Limited myself to 15 minutes
string = 'a1b2c3d4'

def stringdatatype(mystring):
    if(string.isdigit()):
        return 'The string is comprised of digits'
    elif(string.isalnum()):
        return 'The string is comprised of alpha and numeric characters'
    elif(string == TRUE or string == FALSE):
        return 'The string is a boolean value'
    else:
        return 'Unknown string type'

print(stringdatatype(string))

##This was a pretty easy challenge


#Lesson 23 - Classes and Objects (Overview)

##Terms
##
##Class - A user-defined prototype for an object that defines a set of attributes
##that characterize any object of the class. The attributes are data members
##(class variables and instance variables) and methods, accessed via dot notation.
##
##Class Variable - A variable that is shared by all instances of a class.
##Class variables are defined within a class but outside any of the class's
##methods. Class variables are not used as frequently as instance variables are.
##
##Data Member - A class variable or instance variable that holds data associated
##with a class and its objects.
##
##Instance Variable - A variable that is defined inside a method and belongs only
##to the current instance of a class.
##
##Inheritance - The transfer of the characteristics of a class to other classes
##that are derived from it.
##
##Instance - An individual object of a certain class. An object obj that belongs
##to a class Circle, for example, is an instance of the class Circle.
##
##Instantiation − The creation of an instance of a class.
##
##Method - A special kind of function that is defined in a class definition.
##
##Object - A unique instance of a data structure that's defined by its class. An
##object comprises both data members (class variables and instance variables)
##and methods.


#Lesson 24 - Classes and Objects (Using 'Class')
class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
    def display(self):
        print("You're a ", self.gender, ", and your name is: ", self.name)

people = Person('Male', 'Alex')
people.display()


#Lesson 25 - Classes and Objects (Using Methods)
class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
    def display(self):
        print("You're a ", self.gender, ", and your name is: ", self.name)

people = Person('Male', 'Alex')
people2 = Person('Female', 'Joan')
##A method is like calling a function within a class.  Dot allows to call upon an
##attribute of the class.
people.display()
people2.display()
##You don't always to call a value in a function within a class (e.g. self)


#Lesson 26 - Classes and Objects (Using Object Data)
class Example:
    ##one asterisk is for a tuple, two asterisks is for dictionary
    ##kwargs stands for key word arguments
    def __init__(self, **kwargs):
        self.variables = kwargs
    ##Creating function that sets a key in the dictionary to specific values    
    def set_vars(self,key,value):
        self.variables[key] = value
    def get_vars(self,key):
        return self.variables.get(key, None)   

var = Example(Age = 17, Location = 'UK')
var.set_vars('name', 'alex')
print(var.get_vars('name'))
print(var.get_vars('Age'))
print(var.get_vars('Location'))


#Lesson 27 - Classes and Objects (Using Inheritance)
class Animals:
    def eat(self):
        print('I can eat')
    def talk(self):
        print('I can talk')

##Adding animals to the parameter of this class inherits all attributes from the
##Animals class
class Cat(Animals):
    def talk(self):
        print('meow')
    def hairball(self):
        print('Here\'s a hairball!')
class Dog(Animals):
    def talk(self):
        print('woof')
##pass will force the subclass to inherit from parent class        
class Bird(Animals):
    pass

muffin = Cat()
sky = Dog()
polly = Bird()
##we are overriding the animal class talk with cat class talk
muffin.talk()
muffin.hairball()
muffin.eat()

sky.talk()
polly.talk()
