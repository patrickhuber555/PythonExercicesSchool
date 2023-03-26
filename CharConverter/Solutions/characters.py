def is_numeric(char: str) -> bool:
    if (char >= "0") and (char <= "9"):
        return True
    return False


def is_alpha(char: str) -> bool:
    if (is_upper_case(char)) or (is_lower_case(char)):
        return True
    return False


def is_alpha_numeric(char: str) -> bool:
    return (is_numeric(char)) or (is_alpha(char))


def is_upper_case(char: str) -> bool:
    if (char >= "A") and (char <= "Z"):
        return True
    return False


def is_lower_case(char: str) -> bool:
    if (char >= "a") and (char <= "z"):
        return True
    return False


def to_upper_case(char: str) -> str:
    if is_lower_case(char):
        return chr(ord(char) - 32)
    return char


def to_lower_case(char: str) -> str:
    if is_upper_case(char):
        return chr(ord(char) + 32)
    return char


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
