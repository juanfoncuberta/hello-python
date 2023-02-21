from functools import reduce

## Higher Order Functions ##
## pass functions as parameter ##


def sum_one(value):
  return value + 1

def sum_two_value_and_add_one(first_value, second_value,f_sum_one):
  return f_sum_one(first_value+second_value)


print(sum_two_value_and_add_one(20,3,sum_one))



### Closures ###
### Closure is a function that return another function ###


def sum_ten():
  def add(value):
    return value + 10
  return add

print(sum_ten()(3))

def sum_twenty(fist_value):
  def add(second_value):
    return second_value + 20
  return add
  
sum_twenty_closure = sum_twenty(10)
print(sum_twenty_closure(4))


def sum_thirty(fist_value):
  return lambda second_value: 30 + fist_value + second_value

sum_thirty_closure_lambda = sum_thirty(4)
print(sum_thirty_closure_lambda(3))


### Built-in Higher Order Functions ###

numbers = [1,3,6,11,9,33]

def multiply_two(number):
  return number * 2

print(map(multiply_two, numbers))
print(map(lambda number: number * 3, numbers))

def filter_greater_than_ten(number):
  return number > 10

print(filter(filter_greater_than_ten,numbers))
print(filter(lambda number: number > 10,numbers))


def sum_two_values(first_value,second_value):
  print(first_value)
  print(second_value)
  print("-------")
  return first_value + second_value

print(reduce(sum_two_values, numbers))