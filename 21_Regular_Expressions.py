## Regular Expressions ## 

import re

my_string = "I'm Juan & i'm 36 years old"

#Match returns an object if patter found. Only if the string begins with the pattern
match = re.match("I'm",my_string)
no_match = re.match("'m",my_string)
print(match)
print(no_match)
#span return the range of the position
print(match.span())
#error because pattern non found
#print(no_match.span())

#Search return and object match whether  find the pattern or not
search = re.search("I'm",my_string)
no_search = re.search("'m",my_string)
print(search)
print(no_search)
print(search.span())
print(no_search.span())

#findall return the times it found the pattern
findall = re.findall("[I|i]'m", my_string)
print(findall)


#split, splits the string according to the pattern
split = re.split("&",my_string)
print(split)

#sub replaces the first params with the second 
sub = re.sub("I'm", "You're",my_string)
sub_both = re.sub("[I|i]'m", "You're",my_string)
print(sub)
print(sub_both)


#Patterns
pattern = r"[I|i]'m|years"
print(pattern)
print(re.findall(pattern,my_string))
pattern_number = r"[0-9]"
print(pattern_number)
print(re.findall(pattern_number,my_string))
#\d search for number characters
pattern_second = r"\d"
print(re.findall(pattern_second,my_string))
#\d search for all characters less numbers
pattern_third = r"\D"
print(re.findall(pattern_third,my_string))
pattern_a = r"[a]."
print(re.findall(pattern_a,my_string))
pattern_a_second = r"[a].*"
print(re.findall(pattern_a_second,my_string))
pattern_begin_number = r"^[0-9]"
pattern_begin_letter = r"^[a-zA-Z]"
print(re.search(pattern_begin_number,my_string))
print(re.search(pattern_begin_letter,my_string))
pattern_complex_start = r"^[a-zA-Z].[a-zA-Z]"
print(re.search(pattern_complex_start,my_string))
