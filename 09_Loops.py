## Loops ##

# While

my_while_condition = 0

while my_while_condition < 10:
  print(my_while_condition)
  my_while_condition +=1
else:
  print('the while loops has ended')



# For

my_list = ['python','git',"vsc"]

for element in my_list:
  print(element)


#prints the dictionary's keys
my_dict = {"Name":'Juan', 'Lastname': 'Foncuberta','Age': 35, 'Country' : 'Spain'}
for element in my_dict:
  print(element)

#prints the values  
for element in my_dict.values():
  if element == 35:
      continue
  print(element)
else:
  print('all elements have been printed')
