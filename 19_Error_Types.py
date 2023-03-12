### Error types ###

#SyntaxError
#print "¡Hola Comunidad!"
print ("¡Hola Comunidad!")

#NameError
#print (age)
age = 10
print(age)

#IndexError
my_list =  ['python','swift']
#print(my_list[2])
print(my_list[0])

#ModuleNotFoundError
#import maths
import math

#AtributeError
#print(math.PI)
print(math.pi)

#KeyError
my_dict = {"Name":'Juan', 'Lastname': 'Foncuberta'}
# print(my_dict["name"])
print(my_dict["Name"])

#TypeError
#print(my_list["1"])
print(my_list[1])


#ImportError
#from math import PI
#print(PI)
from math import pi
print(pi)

#ValueError
#my_int = int("10 años")
my_int = int("10")
print(my_int)

#ZeroDivisionError
#print(4/0)