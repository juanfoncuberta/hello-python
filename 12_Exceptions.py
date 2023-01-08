## Exceptions Handling ##

"""
The order is:
  try
  except
  else
  finally
"""
first_number, second_number = 5, 1



def addNumbers(first_number,second_number):
  #could catch/filter for error type
  try:
    print(first_number + second_number)
  except OSError as err:
    print("OS error:", err)
  except ValueError:
    print("Could not convert data to an integer.")
  except TypeError as err:
    print(f"Is a {type(err)}")
    print(err)
  except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
  else:
    #Only runs if doesn't catch an error
    print("The code continues running if an error is caught")
  finally:
    #Runs always
    print("The code continues running always")


addNumbers(first_number, second_number)
addNumbers(first_number, "3")