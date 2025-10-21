#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Get the validated number of terms
def user_input():
  while(True):
    print("Enter the number of Fibonacci terms you want: ")
    terms = input()
    if (terms.isdigit()):
      terms = int(terms)
      if (terms > 0):
        break;
      else:
        print("Error: Please enter a positive integer greater than 0")
    else:
      print("Error: Please enter a positive integer greater than 0:")
  return terms

# Generate the sequence
def fibonacci (terms):
  if (terms == 0):
    return 0
  if (terms == 1):
    return 1
  else:
    return fibonacci(terms - 1) + fibonacci (terms - 2)

def print_fib(terms):
  for i in ranage (1, terms + 1):
    print(fibonacci(i), end = " ")

# Print the result
terms = user_input()
fibonacci(terms)
print_fib(terms)
