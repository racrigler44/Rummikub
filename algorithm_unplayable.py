def identify_unplayable_tiles(hand, board):
    """
    Given the hand and board as lists of (color, number) tiles,
    return the list of tiles from the hand that are unplayable.

    A tile is playable if:
    - It can form a set of at least 3 tiles with the same number but different colors (including itself).
    OR
    - It can form a run of at least 3 consecutive numbers of the same color (including itself).
    """
    # Catalog by number → set of colors present (from hand + board)
    number_to_colors = {}
    for color, num in hand + board:
        number_to_colors.setdefault(num, set()).add(color)

    # Catalog by color → sorted list of numbers present (from hand + board)
    color_to_numbers = {}
    for color, num in hand + board:
        color_to_numbers.setdefault(color, set()).add(num)
    for color in color_to_numbers:
        color_to_numbers[color] = sorted(color_to_numbers[color])

    unplayable = []

    for color, num in hand:
        # Check if can form set: need at least 3 different colors with this number
        colors_with_same_num = number_to_colors.get(num, set())
        can_form_set = len(colors_with_same_num) >= 3

        # Check if can form run: need at least two other consecutive numbers with same color
        nums_in_color = color_to_numbers.get(color, [])
        if num not in nums_in_color:
            # If the tile itself is missing (should not happen), mark unplayable
            can_form_run = False
        else:
            idx = nums_in_color.index(num)
            # Count consecutive neighbors around num
            count = 1  # include current tile
            # Check backward neighbors
            if idx >= 1 and nums_in_color[idx - 1] == num - 1:
                count += 1
                if idx >= 2 and nums_in_color[idx - 2] == num - 2:
                    count += 1
            # Check forward neighbors
            if idx + 1 < len(nums_in_color) and nums_in_color[idx + 1] == num + 1:
                count += 1
                if idx + 2 < len(nums_in_color) and nums_in_color[idx + 2] == num + 2:
                    count += 1
            can_form_run = count >= 3

        if not (can_form_set or can_form_run):
            unplayable.append((color, num))

    return unplayable