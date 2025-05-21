def validate_colornumber_input(input_str):
    valid_colors = {"r", "o", "blue", "black"}
    valid_numbers = {str(i) for i in range(1, 14)}  # "1" to "13"

    tokens = input_str.replace(',', ' ').split()

    if len(tokens) == 0:
        return False, "Input cannot be empty."

    parsed_cards = []

    for token in tokens:
        matched = False
        for color in valid_colors:
            if token.startswith(color):
                num_part = token[len(color):]
                if num_part in valid_numbers:
                    parsed_cards.append((color, num_part))
                    matched = True
                    break
        if not matched:
            return False, f"Invalid format: '{token}'"

    return True, "All entries are valid."
