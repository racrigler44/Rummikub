from itertools import combinations

def parse_tiles(group_strs):
    groups = []
    for group_str in group_strs:
        tiles = group_str.strip("{} ").split(",")
        group = []
        for tile in tiles:
            tile = tile.strip()
            color = ''.join(filter(str.isalpha, tile))
            number = int(''.join(filter(str.isdigit, tile)))
            group.append((color, number))
        groups.append(group)
    return groups

def parse_hand(hand_str):
    tiles = hand_str.strip("{} ").split(",")
    hand = []
    for tile in tiles:
        tile = tile.strip()
        color = ''.join(filter(str.isalpha, tile))
        number = int(''.join(filter(str.isdigit, tile)))
        hand.append((color, number))
    return hand

def is_valid_group(group):
    if len(group) < 3:
        return False
    colors = [color for color, _ in group]
    numbers = [num for _, num in group]
    # Set (same number, different colors)
    if len(set(numbers)) == 1 and len(set(colors)) == len(group):
        return True
    # Run (same color, consecutive numbers)
    if len(set(colors)) == 1:
        sorted_nums = sorted(numbers)
        return all(sorted_nums[i] + 1 == sorted_nums[i + 1] for i in range(len(sorted_nums) - 1))
    return False

def find_initial_groups_from_hand(hand):
    groups = []
    used_tiles = set()
    for size in range(3, len(hand) + 1):
        for combo in combinations(hand, size):
            if any(tile in used_tiles for tile in combo):
                continue
            if is_valid_group(combo):
                groups.append(list(combo))
                used_tiles.update(combo)
    remaining_hand = [tile for tile in hand if tile not in used_tiles]
    return groups, remaining_hand

def try_add_tile_to_board(board, hand):
    remaining_hand = []
    for tile in hand:
        added = False
        for group in board:
            new_group = group + [tile]
            if is_valid_group(new_group):
                group.append(tile)
                added = True
                break
        if not added:
            remaining_hand.append(tile)
    return board, remaining_hand

def try_extract_and_combine(board, hand):
    new_board = [g[:] for g in board]
    remaining_hand = hand[:]
    used_tiles = set()

    for combo in combinations(hand, 2):
        if combo[0] in used_tiles or combo[1] in used_tiles:
            continue
        needed_color = combo[0][0]

        if combo[0][0] == combo[1][0]:  # Same color, trying to make a run
            nums = sorted([combo[0][1], combo[1][1]])
            missing = nums[0] + 1
            if nums[1] == nums[0] + 2:
                for group in new_board:
                    for tile in group:
                        if tile == (needed_color, missing):
                            group.remove(tile)
                            if not is_valid_group(group):
                                group.append(tile)
                                continue
                            test_group = list(combo) + [tile]
                            if is_valid_group(test_group):
                                new_board.append(test_group)
                                used_tiles.update(combo)
                                break

        elif combo[0][1] == combo[1][1]:  # Same number, trying to make a set
            needed_num = combo[0][1]
            existing_colors = {combo[0][0], combo[1][0]}
            for group in new_board:
                for tile in group:
                    if tile[1] == needed_num and tile[0] not in existing_colors:
                        group.remove(tile)
                        if not is_valid_group(group):
                            group.append(tile)
                            continue
                        test_group = list(combo) + [tile]
                        if is_valid_group(test_group):
                            new_board.append(test_group)
                            used_tiles.update(combo)
                            break

    final_hand = []
    for t in remaining_hand:
        if not any(t == used for used in used_tiles):
            final_hand.append(t)

    return new_board, final_hand

def try_extract_and_make_new_run(board, hand):
    new_board = [g[:] for g in board]
    modified = False
    hand_used_tiles = []

    for tile_in_hand in hand:
        color, num = tile_in_hand
        if tile_in_hand in hand_used_tiles:
            continue

        for delta in [-2, -1, 1, 2]:
            needed = (color, num + delta)
            for group in new_board:
                if needed in group:
                    group.remove(needed)
                    if not is_valid_group(group):
                        group.append(needed)
                        continue

                    # Determine the third tile in the run
                    if delta == -2:
                        third = (color, num - 1)
                        run = [needed, third, tile_in_hand]
                    elif delta == -1:
                        third = (color, num + 1)
                        run = [needed, tile_in_hand, third]
                    elif delta == 1:
                        third = (color, num - 1)
                        run = [third, tile_in_hand, needed]
                    else:  # delta == 2
                        third = (color, num + 1)
                        run = [tile_in_hand, third, needed]

                    # Check if third is available
                    in_hand = third in hand and third not in hand_used_tiles
                    in_board = False
                    for g in new_board:
                        if third in g:
                            g.remove(third)
                            if not is_valid_group(g):
                                g.append(third)
                                continue
                            in_board = True
                            break

                    if in_hand or in_board:
                        new_board.append(run)
                        hand_used_tiles.append(tile_in_hand)
                        if in_hand:
                            hand_used_tiles.append(third)
                        modified = True
                        break

                    # If not successful, restore the removed tile
                    group.append(needed)

    # Remove used tiles from hand based on exact value match
    final_hand = []
    hand_used_count = {t: hand_used_tiles.count(t) for t in hand_used_tiles}
    for tile in hand:
        if hand_used_count.get(tile, 0) > 0:
            hand_used_count[tile] -= 1
        else:
            final_hand.append(tile)

    return new_board, final_hand, modified

def display_state(board, hand):
    print("Current board:")
    for group in board:
        print("{" + ", ".join(f"{c}{n}" for c, n in group) + "}")
    print("Remaining hand:", "{" + ", ".join(f"{c}{n}" for c, n in hand) + "}")

def play_hand_only_groups(board_strs, hand_str):
    board = parse_tiles(board_strs)
    hand = parse_hand(hand_str)

    # Step 1: Play any full groups directly from the hand
    initial_groups, hand = find_initial_groups_from_hand(hand)
    board.extend(initial_groups)

    # Step 2: Try to add hand tiles directly to existing groups
    board, hand = try_add_tile_to_board(board, hand)

    # Step 3: Try to extract one tile from the board and combine with two in hand
    board, hand = try_extract_and_combine(board, hand)

    # Step 4: Try to make new runs using a hand tile + one board tile
    modified = True
    while modified:
        board, hand, modified = try_extract_and_make_new_run(board, hand)

    return board, hand
