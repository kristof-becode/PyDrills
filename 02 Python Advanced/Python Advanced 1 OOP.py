PYTHON OOP DRILL // Exercise 01 - Dog Inheritance
class Dog:

    # Class attribute
  species = 'mammal'

    # Initializer / Instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # instance method
  def description(self):
    return "{} is {} years old".format(self.name, self.age)

    # instance method
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)

class Pets():
    # Class attribute
  species = 'mammal'
  #list = []

    # Initializer / Instance attributes
  def __init__(self, list):
    self.list = list
    
    # instance method
  def description(self):
    print("I have " + str(len(self.list)) + " dogs.")
    for item in self.list:
      print(item.description()) #refers to dog.description()
    print("They are all " + Pets.species)



d1= Dog("Tom",6)
d2= Dog("Fletcher",7)
d3= Dog("Larry",9)
colPet = Pets([d1,d2,d3])
colPet.description()

returns:
I have 3 dogs.
Tom is 6 years old
Fletcher is 7 years old
Larry is 9 years old
They are all mammal
=============================================================================================
PYTHON OOP DRILL // Exercise 02 - Hungry Dogs

Using the same file, add an instance attribute of is_hungry = True to the Dog class. Then add a method called eat() which changes the value of is_hungry to False when called. Figure out the best way to feed each dog and then output “My dogs are hungry.” if all are hungry or “My dogs are not hungry.” if all are not hungry. The final output should look like this:

I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course. 
My dogs are not hungry.
--------------------------------------


class Dog:

    # Class attribute
  species = 'mammal'
  is_Hungry = True

    # Initializer / Instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # instance method
  def description(self): #added is_Hungry to dog.description() as well
    #return "{} is {} years old and hungry is {}".format(self.name, self.age,self.is_Hungry)
    return "{} is {} years old".format(self.name, self.age)

    # instance method
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)

  def eat(self):
    self.is_Hungry = False

class Pets():#Dog between () ?
    # Class attribute
  species = 'mammal'
  #list = []

    # Initializer / Instance attributes
  def __init__(self, list):
    self.list = list
    
    # instance method: added the last conditional to see if they all hungry, not hungry or some are, some aren't
  def description(self):
    print("I have " + str(len(self.list)) + " dogs.")
    for item in self.list:
      print(item.description())
    print("They are all " + Pets.species + "s, of course")
    if all(item.is_Hungry==True for item in self.list):
      print("My dogs are hungry")
    elif all(item.is_Hungry==False for item in self.list):
      print("My dogs are not hungry")
    else :
      print("Some of my dogs are and some are not hungry")


d1= Dog("Tom",6)
d2= Dog("Fletcher",7)
d3= Dog("Larry",9)
colPet = Pets([d1,d2,d3])
d1.eat()
d2.eat()
d3.eat()
colPet.description()
========================================================================================
PYTHON OOP DRILL // Exercise 03 - Dog Walking

Next, add a walk() method to both the Pets and Dog classes so that when you call the method on the Pets class, each dog instance assigned to the Pets class will walk(). Save this as dog_walking.py. This is slightly more difficult.

Start by implementing the method in the same manner as the speak() method. As for the method in the Pets class, you will need to iterate through the list of dogs, then call the method itself.

The output should look like this:

Tom is walking!
Fletcher is walking!
Larry is walking!
----------------------
class Dog:

    # Class attribute
  species = 'mammal'
  is_Hungry = True

    # Initializer / Instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # instance method
  def description(self): #added is_Hungry to dog.description() as well
    #return "{} is {} years old and hungry is {}".format(self.name, self.age,self.is_Hungry)
    return "{} is {} years old".format(self.name, self.age)

    # instance method
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)

  def eat(self):
    self.is_Hungry = False

  def walk(self): #added walk for EX3
    return "{} is walking.".format(self.name)

class Pets():
    # Class attribute
  species = 'mammal'
  #list = []

    # Initializer / Instance attributes
  def __init__(self, list):
    self.list = list
    
    # instance method
  def description(self):
    print("I have " + str(len(self.list)) + " dogs.")
    for item in self.list:
      print(item.description())
    print("They are all " + Pets.species + "s, of course")
    if all(item.is_Hungry==True for item in self.list):
      print("My dogs are hungry")
    elif all(item.is_Hungry==False for item in self.list):
      print("My dogs are not hungry")
    else :
      print("Some of my dogs are and some are not hungry")
  
  def walk(self): # added EX3, now all dogs can walk, refers to dog.walk()
    for item in self.list:
      print(item.walk())


d1= Dog("Tom",6)
d2= Dog("Fletcher",7)
d3= Dog("Larry",9)
colPet = Pets([d1,d2,d3])
d3.eat()
colPet.description()
#print(d3.walk())
colPet.walk()
=====================================================================
PYTHON OOP DRILL // Exercise 04 - Comprehension Check

Answer the following questions about OOP to check your learning progress:

    What’s a class?
Objects belong to classes. Classes have methiods, spcecific class functions and attributes, specific class variables.
    What’s an instance?
An instance is an instance of class. Class : Car, redspider.Car(), redspider is an object of class Car.
    What’s the relationship between a class and an instance?
see above
    What’s the Python syntax used for defining a new class?
Class 'Name':
    What’s the spelling convention for a class name?
Capital first letter
    How do you instantiate, or create an instance of, a class?
respider.car(red,fast) 
    How do you access the attributes and behaviors of a class instance?
    What’s a method?
A function specific to a class
    What’s the purpose of self?
In the class refer to attributes of the same class by using 'self'.
    What’s the purpose of the init method?
Initialise a certain number of attributes
    Describe how inheritance helps prevent code duplication.
You can call on methods and objects, defined/coded/typed in parents, so less coding required.
    Can child classes override properties of their parents?
No
=======================================================================


