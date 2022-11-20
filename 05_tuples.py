# tuples => immutable

"""
declaration with tuple, just one 1 argument
declaration with (), n arguments accepted
"""
my_tuple = tuple('python')
my_other_tuple = ('python')

print(my_tuple)
print(my_other_tuple)
print(my_tuple == my_other_tuple)



#index => returns the first argument's position
my_tuple = ('kitesurf','running','skiing','paddle','running')
#my_tuple.pop()
print(my_tuple)
index = my_tuple.index('running')
print(index)

"""
tuples can't assign value on positions. Is immutable
to transform to mutable => my_list = list(my_tuple)
"""
#my_tuple[0] = 'hey'  => error
#my_tupple[5] = 'ho'  => error
print(my_tuple)

#delete tuple
del my_tuple
#print(my_tuple)