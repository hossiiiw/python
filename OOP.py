


class Person:
  def __init__(self , name="" , age = 0):
    self.name = name
    self.age = age

  def eat(self):
    print(f"\n{self.name} is eating \nYou are {self.age}")

  def __eq__(self , other):
    return self.name == other.name and self.age == other.age
    



# first_person = Person("hossein",25)
# first_person.eat()
# second_person = Person("asra" , 16)
# second_person.eat()
# third_person = Person()
# third_person.name = "third"
# third_person.age = 30
# third_person.eyecolor= "black"
# third_person.eat()
# print(third_person.eyecolor)

# first_person = Person("hossein",25)
# second_person = Person("hossein",25)
# print(first_person == second_person)


class Animal:
  def __init__(self , name="" , typeOf="" , food=""):
    self.name = name
    self.typeOf = typeOf
    self.food = food

  def eat(self):
    print(f"Type : {self.typeOf}")
    print(f"{self.name} eat {self.food}")


class Mammal(Animal):
  def __init__(self , name ,typeOf, age , weight=""):
    super().__init__(name ,typeOf , age)
    self.weight = weight


  def walk(self):
    print("walk")

  def health(self):
    print(f"{self.weight}")

class Fish(Animal):
  def swim(self):
    print("swim")


dog = Mammal("jessy" , "dog" , "meat" , "1kg")
golden_fish = Fish("golden fish" , "fish" , "vegtibale")
# dog.eat()
# dog.health()

# golden_fish.eat()


class Parent1:
  def feature1(self):
    print("feature1")
  def common(self):
    print("Parent 1 common")

class Parent2:
  def feature2(self):
    print("feature2")
  def common(self):
    print("Parent 2 common")


class Child(Parent1 , Parent2):
  def feature3(self):
    print("child")

  def common(self):
    print("child common")

test = Child()
# test.feature1()
# test.feature2()
# test.common()


# abstract

from abc import ABC , abstractmethod

class Animal(ABC):
  def eat(self):
    return "eat"

  @abstractmethod
  def make_sound(self):
    pass


class Dog(Animal):
  def make_sound(self):
    return "Woof"

class Cow(Animal):
  def eat(self):
    return "eat"
  def make_sound(self):
    return "Bah"

dog = Dog()
# print(dog.make_sound())
cow = Cow()
# print(cow.make_sound())


#polymorfism
class UIControl(ABC):
  @abstractmethod
  def test(self):
    pass
  

class TextBox(UIControl) :
  def test(self):
    print("textBox")

class DropDown(UIControl):
  def test(self):
    print("DropDown")

def test(control):
  control.test()



example= TextBox()
drop = DropDown()
test(example)
test(drop)