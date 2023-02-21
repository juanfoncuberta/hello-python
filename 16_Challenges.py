### Challenges ###

"""
  FIZZBUZZ
  - Multiples of 3 -> Fizz
  - Mutiples of 5 -> Buzz
  - Multiples of 3 and 5 -> FizzBuzz
  """


print("-------Fizzbuzz time --------")

def mod(dividend,divider):
    return dividend % divider

def fizzbuzz(number):
    if(mod(number,3) == 0 and mod(number,5) == 0):
      print("Fizzbuzz")
    elif (mod(number,3) == 0):
      print("Fizz")
    elif (mod(number,5) == 0):
      print("Buzz")
    else:
      print(number)


[fizzbuzz(i) for i in range(1,101)]
print("----------------------")


"""
  ANAGRAM
    -Create a functions return if 2 words are anagrams
"""

print("-------Anagram--------")

def is_anagram(word_one, word_two):
  return not(word_one[::-1] != word_two)

print(is_anagram('roma','amor'))
print("----------------------")


"""
  FIBONACCI 
    -return 50 first numbers of fibonacci sequence
"""

print("-------Fibonacci Sequence--------")
def fibonacci_sequence():
  index = 0
  n1 = fib =  0
  n2 = 1
  while index < 50:
    print(n1)
    fib = n1 + n2
    n1 = n2
    n2 = fib
    index +=1
  
  
fibonacci_sequence()
print("----------------------")

"""
  PRIME NUMBER

"""
print("-------Prime Number--------")
def is_prime_number(number):
  for i in range(2,number):
    if(number % i == 0):
      return False
  return True

print(is_prime_number(7))
print("----------------------")