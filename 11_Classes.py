## Classes ##


## Pass is needed for empty classes. 
class EmptyClass:
  pass


class Person:
  def __init__(self,name,lastname) -> None:
    print(f"A instance of person is created with name: {name} and lastname: {lastname}")
    self.name = name
    self.lastname = lastname
    self.__age = None
    #vars declared with __ are private. Only accessible with functions
    self.__fullname = f"{name} {lastname}"
    pass
  def say_hi(self):
    print(f"Hi {self.name}")

  def get_fullname(self):
    return self.__fullname

  def set_fullname(self,fullname):
    self.__fullname = fullname


  #another way to create getter and setter is with property and @var.setter
  @property
  def age(self):
    return self.__age
  @age.setter #Property SETTER
  def age(self, nuevo):
    print("in")
    self.__age = nuevo

first_person = Person('Juan','Foncuberta')
print(first_person.name)
first_person.say_hi()
print(first_person.get_fullname())
first_person.set_fullname('new fullname')
print(first_person.get_fullname())
print(first_person.age)
first_person.age = 20
print(first_person.age)
