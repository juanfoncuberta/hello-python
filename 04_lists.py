""" 
  lists
  smarter than an array
  list has predefined functions/operationss
"""

#this is a list
my_list = ['python','git',"vsc"]
#this is a list aswell
my_other_list = list('ese')

print(my_list)
print(my_other_list)
print(type(my_list))
print(type(my_other_list))
print(my_other_list[1])
#print(my_other_list[5]) #error out of range

#function counts => Return number of occurrences of value
print(my_list.count('as'))

language, control_version, ide = my_list

print(ide)


#concat list
my_concat_list = my_list + my_other_list
print(my_concat_list)

#append => add value to the list
my_list.append('mac')
print(my_list)

#insert => append in the position x
my_list.insert(2,"freelance")
print(my_list)

"""
remove => removes the value from the list. 
if the value doesn't, breaks
"""
my_list.remove("mac")
print(my_list)
#my_list.remove(2)
#print(my_list)

"""
pop => deletes and return last element
also deletes the index if receives as parameter
"""
last_element = my_list.pop()
print(my_list)
print(last_element)
print(my_list.pop(1))
print(my_list)


#del => the way to delete an element from a list with and indexs
del my_list[1]
print(my_list)


#copy
my_list_copied = my_list.copy()

#clear => deletes the list. works with python > 3
my_list.clear()
print(my_list)

print(my_list_copied)
my_list_copied.append('hi')
print(my_list_copied)

#reverse
my_list_copied.reverse()
print(my_list_copied)




