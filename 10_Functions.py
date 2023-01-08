## Functions ##

def my_function():
  print('this is my first function in python')

my_function()


def add_values(n1,n2):
  return n1 + n2

print(add_values(2,3))
print(add_values("2","3"))
print(add_values(2.4,3))

def print_string(first_word,second_word, default = 'Default word'):
  print(f"First word: {first_word}, Second word: {second_word}. The default word is {default}")


print_string(second_word = "World", first_word = "Hello")
print_string(second_word = "World", first_word = "Hello", default= 'me')



#with * the parameters arrives with a tuple
def print_n_params(*params):
  for element in params:
    print(element)

print_n_params("Hey!")
print_n_params("How", "are", "u", "doing","?")