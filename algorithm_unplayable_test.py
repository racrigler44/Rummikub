import random
from algorithm_unplayable import identify_unplayable_tiles  # your new function

def generate_random_tile():
    colors = ["r", "o", "blue", "black"]
    number = random.randint(1, 13)
    color = random.choice(colors)
    return f"{color}{number}"

def generate_random_run(color, start_num, length):
    return [f"{color}{n}" for n in range(start_num, start_num + length)]

def generate_random_group(number, colors):
    return [f"{color}{number}" for color in colors]

def parse_tiles(tile_str):
    # Helper to convert string like "r1, blue2" to list of (color, num)
    tiles = []
    parts = [t.strip() for t in tile_str.split(",")]
    for part in parts:
        for color in ["r", "o", "blue", "black"]:
            if part.startswith(color):
                num = int(part[len(color):])
                tiles.append((color, num))
                break
    return tiles


# Generate 10 random hand tiles
hand_tiles_str = [generate_random_tile() for _ in range(10)]
hand_str = ", ".join(hand_tiles_str)

# Generate 10 valid sets on board: 5 runs + 5 groups
board_sets = []

for _ in range(5):
    c = random.choice(["r", "o", "blue", "black"])
    start = random.randint(1, 10)
    length = random.choice([3, 4])
    run = generate_random_run(c, start, length)
    board_sets.append("{" + ", ".join(run) + "}")

for _ in range(5):
    num = random.randint(1, 13)
    colors = random.sample(["r", "o", "blue", "black"], random.choice([3,4]))
    group = generate_random_group(num, colors)
    board_sets.append("{" + ", ".join(group) + "}")

board_str = ", ".join(board_sets)

print("Hand:", hand_str)
print("Board:", board_str)

# Parse hand and board tiles for algorithm input
hand = parse_tiles(hand_str)
board = []
for group_str in board_str.split("},"):
    group_str = group_str.strip().strip("{} ")
    if group_str:
        board.append(parse_tiles(group_str))

# Flatten board tiles (list of tuples)
flat_board = [tile for group in board for tile in group]

# Identify unplayable tiles in the hand
unplayable = identify_unplayable_tiles(hand, flat_board)

print("\nUnplayable tiles in hand (cannot form groups or runs):")
print(", ".join(f"{c}{n}" for c, n in unplayable))

print("\nDone running unplayable tile identification.")
