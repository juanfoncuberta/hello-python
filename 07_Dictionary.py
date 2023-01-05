## Dictionaries ##

my_dict = dict()
print(type(my_dict))

my_dict = {}
print(type(my_dict))

my_dict = {"Name":'Juan', 'Lastname': 'Foncuberta'}
print(my_dict)

my_dict['languages'] = {"Python", 'Javascript'}
print(my_dict)


print(len(my_dict))
print(len(my_dict['languages']))

#my_dict.pop() -> got error. Needs at least one parameter
my_dict.pop('Name')
print(my_dict)


#for 'in', py search for key, not for value
print('Lastname' in my_dict)
print('Foncuberta' in my_dict)


#gets all key/val separated in sets
print(my_dict.items())
#gets all the keys
print(my_dict.keys())
#gets all the values
print(my_dict.values())


#fromkeys create new object with the selected keys but with empty values
my_second_dict = my_dict.fromkeys(my_dict.keys())
print(my_second_dict)

#having second parameters you assign the values to each key
my_second_dict = my_dict.fromkeys(my_dict.keys(),my_dict.values()) 
print(my_second_dict)

del my_dict
#print(my_dict) -> got error, my_dict is not defined