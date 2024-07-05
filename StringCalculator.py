class NegativeNumberException(Exception):
    pass


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
        negatives, positives, current_number, is_negative = validate_character(char, current_number, negatives,
                                                                               positives, is_negative)
    if current_number:
        add_items_to_list(negatives, positives, current_number, is_negative)
    return positives, negatives


def add_items_to_list(negatives, positives, current_number, is_negative):
    number = int(current_number) * (-1 if is_negative else 1)
    required_list = positives if not is_negative else negatives
    required_list.append(number)


def validate_list_items(positives, negatives):
    if negatives:
        raise_exception(negatives)
    return [num for num in positives if num <= 1000]


def raise_exception(negatives):
    raise NegativeNumberException(f"negatives not allowed: {negatives}")


def validate_character(char, current_number, negatives, positives, is_negative):
    char_type_handlers = {'digit': handle_digit, 'minus': handle_minus, 'default': handle_default}
    char_type = 'digit' if char.isdigit() else 'minus' if char == '-' else 'default'
    current_number, is_negative = char_type_handlers[char_type](current_number, is_negative, char)

    if not char.isdigit() and char != '-':
        negatives, positives, current_number, is_negative = handle_non_digits(current_number, negatives, positives, is_negative)
    return negatives, positives, current_number, is_negative


def handle_non_digits(current_number, negatives, positives, is_negative):
    if current_number:
        add_items_to_list(negatives, positives, current_number, is_negative)
    current_number, is_negative = '', False
    return negatives, positives, current_number, is_negative

def handle_digit(current_number, is_negative, char):
    return current_number + char, is_negative


def handle_minus(current_number, is_negative, char):
    return current_number, True


def handle_default(current_number, is_negative, char):
    return current_number, is_negative
