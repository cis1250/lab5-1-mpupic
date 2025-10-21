#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions

# Get the validated number of terms
def user_input():
    while True:
        terms_str = input("Enter the number of Fibonacci terms you want: ")
        
        if terms_str.isdigit():
            terms = int(terms_str)
            if terms > 0:
                return terms
            else:
                print("Error: Please enter a positive integer greater than 0")
        else:
            print("Error: Invalid input. Please enter a whole number.")

# Generate the sequence
def fibonacci_sequence(terms):
    if terms == 1:
        return [0]
    if terms == 2:
        return [0, 1]

    sequence = [0, 1]

    for _ in range(2, terms):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

def print_fib(sequence):
    print("\nFibonacci Sequence:")

    output = " -> ".join(map(str, sequence))
    print(output)

def main():
    num_terms = user_input()
    
    fib_list = fibonacci_sequence(num_terms)
    
    print_fib(fib_list)

if __name__ == "__main__":
    main()
