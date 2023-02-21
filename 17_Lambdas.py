## Lambas ##
## Functions with a unique expression ##

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2,4))

def sum_three_values_with_lamba(value):
    return lambda first_value, second_value: first_value + second_value + value


#the first parameter is the value passed by value to the function. The second and the third are the 'lambas parameters (first_value and second_value)'
print(sum_three_values_with_lamba(4)(1,10))