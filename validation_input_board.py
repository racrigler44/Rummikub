def validate_colornumber_input_board(input_str):
    import re

    valid_colors = {"r", "o", "blue", "black"}
    valid_numbers = set(range(1, 14))  # 1 to 13

    # Extract all sets inside {...}
    sets = re.findall(r"\{([^}]+)\}", input_str)
    if not sets:
        return False, "Input must contain at least one set in curly braces."

    for set_str in sets:
        tokens = set_str.replace(',', ' ').split()
        if not tokens:
            return False, "One of the sets is empty."

        parsed_cards = []
        for token in tokens:
            matched = False
            for color in valid_colors:
                if token.startswith(color):
                    num_part = token[len(color):]
                    if num_part.isdigit() and int(num_part) in valid_numbers:
                        parsed_cards.append((color, int(num_part)))
                        matched = True
                        break
            if not matched:
                return False, f"Invalid format: '{token}'"

        # Check for duplicates
        if len(parsed_cards) != len(set(parsed_cards)):
            return False, f"Duplicate cards found in set '{set_str}'."

        colors = {color for color, _ in parsed_cards}
        numbers = [num for _, num in parsed_cards]

        # Validate as Set (same color, consecutive numbers)
        if len(colors) == 1:
            if len(parsed_cards) < 3:
                return False, f"Set '{set_str}' must have at least 3 tiles."
            numbers_sorted = sorted(numbers)
            for i in range(len(numbers_sorted) - 1):
                if numbers_sorted[i + 1] != numbers_sorted[i] + 1:
                    return False, f"Numbers in set '{set_str}' are not consecutive."
        # Validate as Group (same number, different colors)
        elif len(set(numbers)) == 1:
            if len(parsed_cards) < 3 or len(parsed_cards) > 4:
                return False, f"Group '{set_str}' must have 3 or 4 tiles."
            if len(colors) != len(parsed_cards):
                return False, f"Colors in group '{set_str}' are not unique."
        else:
            return False, f"Set '{set_str}' is neither a valid set nor a valid group."

    return True, "All sets and groups are valid."
