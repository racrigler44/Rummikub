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


def is_valid_set(group):
    if len(group) < 3:
        return False
    numbers = set(num for _, num in group)
    colors = [color for color, _ in group]

    # Valid group: all same number, all different colors
    if len(numbers) == 1 and len(set(colors)) == len(group):
        return True

    # Valid run: same color, consecutive numbers
    if len(set(colors)) == 1:
        sorted_nums = sorted(num for _, num in group)
        return all(sorted_nums[i] + 1 == sorted_nums[i + 1] for i in range(len(sorted_nums) - 1))

    return False

def flatten(groups):
    return [tile for group in groups for tile in group]

def regroup_with_tile_min_hand_use(candidate_tile, hand_tiles, board_sets):
    # Step 1: Try to directly add candidate tile to an existing group
    for i, group in enumerate(board_sets):
        new_group = group + [candidate_tile]
        if is_valid_set(new_group):
            new_board = board_sets[:i] + [new_group] + board_sets[i+1:]
            return True, new_board

    # Step 2: Try rearranging board + candidate_tile + minimal hand tiles
    board_tiles = flatten(board_sets)

    # Prioritize regrouping with just board + candidate
    pool = board_tiles + [candidate_tile]

    def try_build(groups_so_far, tiles_left, hand_left, best_solution):
        if not tiles_left:
            if any(candidate_tile in group for group in groups_so_far):
                return groups_so_far  # Valid solution found
            return best_solution

        for size in range(3, len(tiles_left) + 1):
            for combo in combinations(tiles_left, size):
                if is_valid_set(combo):
                    remaining = [t for t in tiles_left if t not in combo]
                    result = try_build(groups_so_far + [list(combo)], remaining, hand_left, best_solution)
                    if result:
                        return result  # Return on first valid result

        # If no set from current tiles, try adding 1 hand tile at a time
        if hand_left:
            for i, tile in enumerate(hand_left):
                new_tiles = tiles_left + [tile]
                new_hand = hand_left[:i] + hand_left[i+1:]
                result = try_build(groups_so_far, new_tiles, new_hand, best_solution)
                if result:
                    return result

        return best_solution

    result = try_build([], pool, [t for t in hand_tiles if t != candidate_tile], None)
    if result:
        return True, result

    return False, board_sets
