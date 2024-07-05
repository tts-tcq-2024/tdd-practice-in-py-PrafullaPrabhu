def add(inp):
    if not inp:
        return 0
    else:
        return get_output(inp)


def get_output(input_string):
    positives, negatives = extract_numbers_from_string(input_string)
    validated_list = validate_list_items(positives, negatives)
    return sum(validated_list)


def extract_numbers_from_string(input_string):
    positives, negatives = [], []
    current_number, is_negative = '', False
    for char in input_string:
        negatives, positives, current_number, is_negative = validate_character(char, current_number, negatives, positives, is_negative)
    if current_number:
        add_items_to_list(negatives, positives, current_number, is_negative)
    return positives, negatives


def add_items_to_list(negatives, positives, current_number, is_negative):
    number = int(current_number) * (-1 if is_negative else 1)
    required_list = positives if not is_negative else negatives
    required_list.append(number)


def validate_list_items(positives, negatives):
    if negatives:
        raise NegativeNumberException(negatives)
    filtered_numbers = [num for num in positives if num <= 1000]
    return filtered_numbers


def validate_character(char, current_number, negatives, positives, is_negative):
    if char.isdigit() or (char == '-' and not current_number):
        current_number, is_negative = check_character_type(char, current_number, is_negative)
    else:
        if current_number:
            add_items_to_list(negatives, positives, current_number, is_negative)
        current_number = ''
        is_negative = False
    return negatives, positives, current_number, is_negative


def check_character_type(char, current_number, is_negative):
    if char.isdigit():
        current_number += char
    elif char == '-' and not current_number:
        is_negative = True
    return current_number, is_negative


class NegativeNumberException(Exception):
    def __init__(self, negative_numbers):
        super().__init__(f"negatives not allowed: {negative_numbers}")

