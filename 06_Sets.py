##Sets## 

my_set = set()
print(type(my_set))

my_other_set = {}
print(type(my_other_set)) #init as a dict (dictionary)
my_other_set = {'hey': "how"}
print(type(my_other_set)) #init with 'key':'value' is a dict


my_other_set = {'juan','coco'}
print(type(my_other_set)) #if init with a values is a set
print(len(my_other_set))


my_other_set.add('pepe')
print(my_other_set) #set is a list 'disordered'

my_other_set.add('coco')
print(my_other_set) #doesn't repeat values

print("coco" in my_other_set)
print("kai" in my_other_set)


my_other_set.remove('pepe')
print(my_other_set) 

##my_other_set.remove('kai') => error... value not finded


my_other_set.clear()
print(my_other_set) 

my_other_set = {'panx','kai','marta'}
my_team = {'juan','coco'}
print(my_other_set)
print(my_team)


house_team = my_team.union(my_other_set)
print(house_team)

print(house_team.difference(my_team))