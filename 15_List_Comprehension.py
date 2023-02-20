### List Comprehension ###

my_original_list = [0,1,2,3,4,5,6,7]

my_list = [i for i in my_original_list]
print(my_list)

my_second_list = [i*2 for i in range(8)]
print(my_second_list)

def sum_five(number):
  return number + 5
my_third_list = [sum_five(i) for i in range(8)]
print(my_third_list)