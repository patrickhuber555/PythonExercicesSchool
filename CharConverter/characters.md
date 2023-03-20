# Exercise

In this exercise, you have to use the datatype **str** to convert/check certain char values.

Implement the following checks:

def is_numeric(character: str) -> bool:

def is_alpha(character: str) -> bool:

def is_alpha_numeric(character: str) -> bool:

def is_upper_case(character: str) -> bool:

def is_lower_case(character: str) -> bool:

These functions should return **true** or **false**.

Meaning of the function names:

- Numeric: 0-9 (digits)
- Alpha: a-z, A-Z (alphabeth characters)
- Upper Case: A-Z
- Lower Case: a-z

Note:

The shift from **Upper Case** to **Lower Case** is 32 in the ASCII table.  

E.g. 'A' -> 'a' by subtracting 32
E.g. 'a' -> 'A' by adding 32

You do not have to look up the ASCII table for this exercise, but you can do so.

Afterward, implement the following conversion functions:

def to_upper_case(character: str) -> str:

def to_lower_case(character: str) -> str:

These should return the **converted** character.

## Main Function

def main():
    input_character = input("Please enter any ASCII character: ")
    print(f"numeric: {is_numeric(input_character)}")
    print(f"alpha: {is_alpha(input_character)}")
    print(f"alpha_numeric: {is_alpha_numeric(input_character)}")
    print(f"upper_case: {is_upper_case(input_character)}")
    print(f"lower_case: {is_lower_case(input_character)}")
    print(f"to_upper_case: {to_upper_case(input_character)}")
    print(f"to_lower_case: {to_lower_case(input_character)}")
