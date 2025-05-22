from play_exclusive import parse_tiles, regroup_with_tile_min_hand_use

def format_tile(tile):
    return f"{tile[0]}{tile[1]}"

def format_group(group):
    return ", ".join(format_tile(tile) for tile in sorted(group))

def print_board_state(label, board_sets):
    print(f"\n{label}:")
    for group in board_sets:
        print("  {" + format_group(group) + "}")

def test_play_blue4_verbose():
    # Setup: Board has two runs of 4,5,6 in black and orange, and a group of 7s
    board_str = "{black4, black5, black6}, {orange4, orange5, orange6}, {black7, orange7, blue7}"
    hand_str = "{blue4, red5, red6, red7, red9}"

    board_sets = parse_tiles(board_str)
    hand_tiles = parse_tiles(hand_str)[0]
    tile_to_play = ("blue", 4)

    print_board_state("Initial Board", board_sets)
    print("\nHand:", ", ".join(format_tile(tile) for tile in hand_tiles))
    print("\nAttempting to play exclusive tile:", format_tile(tile_to_play))

    success, new_board = regroup_with_tile_min_hand_use(tile_to_play, hand_tiles, board_sets)

    if success:
        print_board_state("Final Rearranged Board", new_board)

        all_played_tiles = [tile for group in new_board for tile in group]
        remaining_hand = [tile for tile in hand_tiles if tile not in all_played_tiles]

        print("\nRemaining Hand Tiles:", ", ".join(format_tile(t) for t in remaining_hand) or "None")

        expected_groups = [
            sorted(["black4", "orange4", "blue4"]),
            sorted(["black5", "orange5", "red5"]),
            sorted(["black6", "orange6", "red6"]),
            sorted(["black7", "orange7", "blue7"]),
        ]

        final_groups = [sorted(format_tile(tile) for tile in group) for group in new_board]
        for expected in expected_groups:
            assert expected in final_groups, f"Expected group {expected} not found"

        assert ("blue", 4) not in remaining_hand, "blue4 should have been played"
        print("\n✅ Test passed. blue4 was successfully played and board rearranged.")

    else:
        print("\n❌ Test failed. Tile could not be played.")
        assert False, "Expected tile to be playable"

def test_play_red8():
    board_str = "{blue8, orange8, black8}"
    hand_str = "{red8, red9, black9}"

    board_sets = parse_tiles(board_str)
    hand_tiles = parse_tiles(hand_str)[0]
    tile_to_play = ("red", 8)

    print_board_state("\n\nInitial Board (Test 2)", board_sets)
    print("Hand:", ", ".join(format_tile(tile) for tile in hand_tiles))
    print("Attempting to play exclusive tile:", format_tile(tile_to_play))

    success, new_board = regroup_with_tile_min_hand_use(tile_to_play, hand_tiles, board_sets)

    if success:
        print_board_state("Final Rearranged Board (Test 2)", new_board)

        all_played_tiles = [tile for group in new_board for tile in group]
        remaining_hand = [tile for tile in hand_tiles if tile not in all_played_tiles]

        print("Remaining Hand Tiles:", ", ".join(format_tile(t) for t in remaining_hand) or "None")

        assert sorted(["blue8", "orange8", "black8", "red8"]) in [
            sorted(format_tile(tile) for tile in group) for group in new_board
        ], "Expected group of four 8s not found"

        assert ("red", 8) not in remaining_hand, "red8 should have been played"
        print("✅ Test passed. red8 was successfully played.")
    else:
        print("❌ Test failed. red8 could not be played.")
        assert False, "Expected red8 to be playable"

def test_simple_play():
    board_str = "{red3, red4, red5}"  # run of red 3,4,5 on board
    hand_str = "{red2}"               # hand has red2, which can extend the run

    board_sets = parse_tiles(board_str)
    hand_tiles = parse_tiles(hand_str)[0]
    tile_to_play = ("red", 2)

    print_board_state("Initial Board", board_sets)
    print("Hand:", ", ".join(format_tile(tile) for tile in hand_tiles))
    print("Attempting to play tile:", format_tile(tile_to_play))

    success, new_board = regroup_with_tile_min_hand_use(tile_to_play, hand_tiles, board_sets)

    if success:
        print_board_state("Final Rearranged Board", new_board)
        remaining_hand = [tile for tile in hand_tiles if tile != tile_to_play]
        print("Remaining hand:", ", ".join(format_tile(t) for t in remaining_hand) or "None")
        assert tile_to_play not in remaining_hand, f"{format_tile(tile_to_play)} should have been played"
        print("✅ Test passed: tile played successfully.")
    else:
        print("❌ Test failed: tile could not be played.")
        assert False, "Expected tile to be playable"


def test_play_red3_complex_rearrangement():
    board_str = "{blue2, blue3, blue4}, {orange2, orange3, orange4}, {black2, black3, black4}"
    hand_str = "{red3, red4, black10}"

    board_sets = parse_tiles(board_str)
    hand_tiles = parse_tiles(hand_str)[0]
    tile_to_play = ("red", 3)

    print_board_state("\n\nInitial Board (New Complex Test)", board_sets)
    print("Hand:", ", ".join(format_tile(tile) for tile in hand_tiles))
    print("Attempting to play exclusive tile:", format_tile(tile_to_play))

    success, new_board = regroup_with_tile_min_hand_use(tile_to_play, hand_tiles, board_sets)

    if success:
        print_board_state("Final Rearranged Board (New Complex Test)", new_board)

        all_played_tiles = [tile for group in new_board for tile in group]
        remaining_hand = [tile for tile in hand_tiles if tile not in all_played_tiles]

        print("Remaining Hand Tiles:", ", ".join(format_tile(t) for t in remaining_hand) or "None")

        # Check the group of 3s is there with red3 and orange3 included
        assert any(sorted(format_tile(tile) for tile in group) == sorted(["blue2", "orange2", "black2"]) for group in new_board), \
            "Expected group of 2s not found"

        

        # Confirm red3 was played (not in remaining hand)
        assert ("red", 3) not in remaining_hand, "red3 should have been played"
        assert ("black", 10) in remaining_hand, "black10 should in the remaining hand"
        print("✅ New complex test passed. red3 was successfully played with proper rearrangement.")
    else:
        print("❌ New complex test failed. red3 could not be played.")
        assert False, "Expected red3 to be playable with rearrangement"


if __name__ == "__main__":
    test_play_blue4_verbose()
    test_simple_play()
    test_play_red3_complex_rearrangement()