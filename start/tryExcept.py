'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

# #The try block will generate an error, because x is not defined:
# try:
#   print(x)
# except:
#   print("An exception occurred")


# #The try block will generate a NameError, because x is not defined:
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


#The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# #The finally block gets executed no matter if the try block raises any errors or not:
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  


# # Raise an error and stop the program if x is lower than 0:
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# You can define what kind of error to raise, and the text to print to the user.
# Example: Raise a TypeError if x is not an integer:
x = "hello"
if type(x) is not int:
  raise TypeError("Only integers are allowed")