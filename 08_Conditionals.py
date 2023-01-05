## Conditionals ##

my_boolean = True

#the negation is python is with 'not'. Not with '!'
if not my_boolean:
  print('my boolean es verdad')
else:
  print("my boolean es false")



my_name = 'Juan'

if len(my_name) > 10:
  print("My name leng is longer than 10 chars.")
elif len(my_name) == 10:
  print("My name leng is 10 chars")
else:
  print("My name leng is shorter than 10 chars")



my_other_boolean = False

if my_boolean and my_other_boolean:
  print("Both vars are true")

if my_boolean or my_other_boolean:
  print("Either vars are true")


my_string = ''
if my_string:
  print("my strinbng isn't empty")

my_string = 'some chars'
if my_string:
  print("my strinbng isn't empty 2")

  

