# Variables. Always with snakecase convention

my_string_var = "My string variable"
print(my_string_var)


my_int_var = 5
print(my_int_var)

my_int_to_str_var = str(my_int_var)
print(my_int_to_str_var)
print(type(my_int_var))
print(type(my_int_to_str_var))
print(type(int(my_int_to_str_var)))

my_list = ["Hello", "World"]
print(my_list[0],my_list[1])

#Variables assignment in one linea

first_word, second_word = 'Hello', 'World'
print("My first word '",first_word,"',and my second word: '",second_word,"'")


#Variables assignment  by shell
first_name = input("What's your name?")
print(first_name)