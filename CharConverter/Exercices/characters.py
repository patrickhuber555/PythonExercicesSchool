def is_numeric(char: str) -> bool:
    # Please enter your code here
    return True


def is_alpha(char: str) -> bool:
    # Please enter your code here
    return True


def is_alpha_numeric(char: str) -> bool:
    # Please enter your code here
    return True


def is_upper_case(char: str) -> bool:
    # Please enter your code here
    return True


def is_lower_case(char: str) -> bool:
    # Please enter your code here
    return True


def to_upper_case(char: str) -> str:
    # Please enter your code here
    return "here comes the **converted** character"


def to_lower_case(char: str) -> str:
    # Please enter your code here
    return "here comes the **converted** character"


def main():
    input_character = input("Please enter any ASCII character: ")
    print(f"numeric: {is_numeric(input_character)}")
    print(f"alpha: {is_alpha(input_character)}")
    print(f"alpha_numeric: {is_alpha_numeric(input_character)}")
    print(f"upper_case: {is_upper_case(input_character)}")
    print(f"lower_case: {is_lower_case(input_character)}")
    print(f"to_upper_case: {to_upper_case(input_character)}")
    print(f"to_lower_case: {to_lower_case(input_character)}")


if __name__ == "__main__":
    main()
