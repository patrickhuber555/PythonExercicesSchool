def modulo(number_a: int, number_b: int) -> int:
    result = 0
    if number_b == 0:
        return 0
    divisor = number_a // number_b
    result = number_a - (number_b * divisor)
    return result


def sum_of_digits(number: int) -> int:
    num_digits = 0
    while number > 0:
        number //= 10
        num_digits += 1
    return num_digits


def cross_sum(number: int) -> int:
    sum = 0
    current_digit = 0
    while number > 0:
        current_digit = number % 10
        sum += current_digit
        number //= 10
    return sum


def main():
    input_number = input("Please enter an integer: ")
    input_number = int(input_number)
    print(f"{input_number} % 3: {modulo(input_number, 3)}")
    print(f"sum_of_digits: {sum_of_digits(input_number)}")
    print(f"cross_sum: {cross_sum(input_number)}")


if __name__ == "__main__":
    main()
