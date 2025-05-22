from algorithm_exclusive import parse_tiles, identify_exclusive_tiles

def tiles_str_to_tuples(tiles_str):
    parsed = parse_tiles(tiles_str)
    return [tile for group in parsed for tile in group]

# === Fixed Board Sets ===

# 5 runs (4 consecutive numbers, same color)
runs = [
    "{r1, r2, r3, r4}",
    "{o5, o6, o7, o8}",
    "{blue9, blue10, blue11, blue12}",
    "{black2, black3, black4, black5}",
    "{r10, r11, r12, r13}"
]

# 5 groups (4 tiles of the same number, different colors)
groups = [
    "{r7, o7, blue7, black7}",
    "{r9, o9, blue9, black9}",
    "{r6, o6, blue6, black6}",
    "{r11, o11, blue11, black11}",
    "{r13, o13, blue13, black13}"
]

board_tiles_str = ", ".join(runs + groups)

# === Fixed Hand Tiles (15) ===
hand_tiles_str = "r7, black1, o12, blue3, black6, o10, r5, blue2, r13, black11, o1, blue5, o9, r8, blue10"

# === Print Setup ===
print("Hand (string):", hand_tiles_str)
print("Board (string):", board_tiles_str)

# === Parse Tiles ===
hand_tiles = tiles_str_to_tuples("{" + hand_tiles_str + "}")
board_tiles = tiles_str_to_tuples(board_tiles_str)

# === Run Exclusive Tile Identification ===
exclusive_tiles = identify_exclusive_tiles(hand_tiles, board_tiles)

# === Print Results ===
print("\nExclusive tiles in hand (only one valid placement):")
if exclusive_tiles:
    for (color, number), reason in exclusive_tiles:
        print(f"- {color}{number}: {reason}")
else:
    print("None")

print("\nDone running exclusive tile identification.")
