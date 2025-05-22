from itertools import combinations

def parse_tiles(tiles_str):
    groups = tiles_str.split("},")
    parsed_groups = []
    for group in groups:
        group = group.strip(" {}")
        if not group:
            continue
        tiles = group.split(",")
        parsed_group = []
        for tile in tiles:
            tile = tile.strip()
            color = ''.join(filter(str.isalpha, tile))
            number = int(''.join(filter(str.isdigit, tile)))
            parsed_group.append((color, number))
        parsed_groups.append(parsed_group)
    return parsed_groups

def identify_exclusive_tiles(hand_tiles, board_tiles):
    """
    Identify tiles from hand that have exactly one valid placement on the board,
    excluding placements that would replace an identical tile already on the board.

    Returns a list of tuples:
    (hand_tile, description_of_board_tiles_supporting_exclusivity)
    """
    board_by_number = {}
    board_by_color = {}
    board_tile_set = set(board_tiles)  # Used to avoid replacements

    for color, number in board_tiles:
        board_by_number.setdefault(number, set()).add(color)
        board_by_color.setdefault(color, set()).add(number)

    exclusive_tiles = []

    for tile in hand_tiles:
        color, number = tile

        if tile in board_tile_set:
            continue  # Skip if this exact tile already exists on the board

        possible_set_colors = board_by_number.get(number, set()) - {color}
        colors_in_board = board_by_color.get(color, set())

        run_positions = []
        if (number - 1) in colors_in_board and (number - 2) in colors_in_board:
            run_positions.append((number - 2, number - 1, number))
        if (number - 1) in colors_in_board and (number + 1) in colors_in_board:
            run_positions.append((number - 1, number, number + 1))
        if (number + 1) in colors_in_board and (number + 2) in colors_in_board:
            run_positions.append((number, number + 1, number + 2))

        set_possibilities = 0
        set_combos = []

        for size in [2, 3]:
            for combo in combinations(possible_set_colors, size):
                set_possibilities += 1
                set_combos.append(combo)

        total_placements = set_possibilities + len(run_positions)

        if total_placements == 1:
            # Determine description of supporting tiles
            if set_possibilities == 1 and not run_positions:
                # Exclusive due to one valid set
                colors_in_set = set_combos[0]
                supporting_tiles = [f"{c}{number}" for c in colors_in_set]
                description = f"Set with tiles: {', '.join(supporting_tiles)}"
            elif not set_possibilities and len(run_positions) == 1:
                # Exclusive due to one valid run
                run = run_positions[0]
                supporting_tiles = [f"{color}{n}" for n in run if n != number]
                description = f"Run with tiles: {', '.join(supporting_tiles)}"
            else:
                # One combo exists that mixes sets and runs (rare but possible)
                desc_parts = []
                if set_possibilities > 0:
                    sets_tiles = []
                    for combo in set_combos:
                        sets_tiles.extend([f"{c}{number}" for c in combo])
                    desc_parts.append(f"Set with tiles: {', '.join(set(sets_tiles))}")
                if run_positions:
                    runs_tiles = []
                    for run in run_positions:
                        runs_tiles.extend([f"{color}{n}" for n in run if n != number])
                    desc_parts.append(f"Run with tiles: {', '.join(set(runs_tiles))}")
                description = " and ".join(desc_parts)

            exclusive_tiles.append((tile, description))

    return exclusive_tiles
