# Strings

"""
  Can be assigned with quotes or double quotes
"""
my_first_string = 'My first string'
my_other_string = "My other string"

# get number of chars
print(len(my_first_string))

# concat strings
print(my_first_string + my_other_string)

# linea break
print("This is a \nline break")

#tabs
print("\tThis is a tab")

#special char scaping
print("\\t Tab scaped")

#formating strings
language, year, ide = "Python",2022,"vsc"

print("It's {}, I'm coding {} with {}".format(year,language,ide))
print("It's %d, I'm coding %s with %s"%(year,language,ide))
print(f"It's {year}, I'm coding {language} with {ide}")

#unpacket chars
a,b,c,d,e,f = language

print(a)
print(b)
print(f)

#slicing
print(language[0:3])
print(language[-3:-2])
print(language[::-1])


#example string functions
print(ide.capitalize())
print(ide.upper())
print(ide.count('s'))
print(ide.isnumeric())
print(language.lower())

