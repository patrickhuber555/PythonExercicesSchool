def modulo(number_a: int, number_b: int) -> int:
    return "returns the result of modulo"

def sum_of_digits(number: int) -> int:
    return "returns the number of the digits"

def cross_sum(number: int) -> int:
    return "returns the cross sum of the given integer"

def main():
    input_number = input("Please enter an integer: ")
    print(f'{input_number} % 3: {modulo(input_number, 3)}')
    print(f'sum_of_digits: {sum_of_digits(input_number)}')
    print(f'cross_sum: {cross_sum(input_number)}')

if __name__ == "__main__":
    main()