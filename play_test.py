# play_test.py
from play import play_hand_only_groups, display_state

def test_case_1():
    board_strs = [
        "{black4, black5, black6}",
        "{orange4, orange5, orange6}",
        "{black7, orange7, blue7}"
    ]
    hand_str = "{blue4, red5, red6, red7, red9}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 1:")
    display_state(board, hand)
    print("\n")

def test_case_2():
    board_strs = [
        "{blue3, blue4, blue5}",
        "{red9, blue9, orange9}"
    ]
    hand_str = "{blue6, black9, red8, red10, red11, orange10, orange11}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 2:")
    display_state(board, hand)
    print("\n")

def test_case_3():
    board_strs = []
    hand_str = "{red3, red4, red5, blue7, black7, orange7, black10, black11, black12}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 3:")
    display_state(board, hand)
    print("\n")
def test_case_4():
    board_strs = ["{black3, black4, black5}", "{red5, red6, red7}"]
    hand_str = "{black6, black7, red4, red3, red8}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 4:")
    display_state(board, hand)
    print("\n")


def test_case_5():
    board_strs = ["{black3, black4, black5}", "{blue4, red4, black4, orange4}"]
    hand_str = "{black6, black7, orange3, orange5}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 5:")
    display_state(board, hand)
    print("\n")

def test_case_6():
    board_strs = ["{black3, black4, black5, black6}", "{blue4, red4, black4, orange4}"]
    hand_str = "{black5}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 6:")
    display_state(board, hand)
    print("\n")

def test_case_7():
    board_strs = ["{black3, black4, black5, black6, black7}"]
    hand_str = "{black5}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 6:")
    display_state(board, hand)
    print("\n")

def test_case_8():
    board_strs = ["{black3, black4, black5, black6, black7}", "{blue4, red4, black4, orange4}"]
    hand_str = "{black5}"
    board, hand = play_hand_only_groups(board_strs, hand_str)
    print("Test Case 7:")
    display_state(board, hand)
    print("\n")

def test_all():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()
if __name__ == "__main__":
    test_all()
