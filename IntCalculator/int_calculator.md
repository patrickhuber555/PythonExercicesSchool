# Exercise

In this exercise, you have to use an **int** datatype for certain computations.

Implement the following functions:

def def modulo(number_a: int, number_b: int) -> int:

def sum_of_digits(number: int) -> int:

def cross_sum(number: int) -> int:

- Modulo
  - Implement the modulo operator (a % b = c)
  - E.g. 10 % 4 = 2, 10 % 3 = 1, 10 % 2 = 0
  
- Sum Of Digits
  - Number of decimal digits
  - E.g. 128 = 3 Digits
  
- Cross Sum (*Quersumme*)
  - Add up all decimal digits
  - E.g. 123 = 6, 1234 = 10

Note:
Int, or integer in Python, is a whole number, positive or negative, without decimals, of unlimited length.

## Main Function

def main():
    input_number = 0

    input_number = input("Please enter an integer: ")
    print(f'{input_number} % 3: {modulo(input_number, 3)}')
    print(f'sum_of_digits: {sum_of_digits(input_number)}')
    print(f'cross_sum: {cross_sum(input_number)}')
