from validation_input_board import validate_colornumber_input_board  # Import from separate file
def run_tests():
    test_cases = [
        # Valid sets (same color, consecutive numbers)
        ("{r1, r2, r3}", True),
        ("{blue10, blue11, blue12, blue13}", True),
        # Invalid set (only 2 or 1 tiles)
        ("{black5, black6}", False),  # Invalid set (only 2 tiles)
        ("{o7}", False),  # Invalid set (only 1 tile)

        # Valid groups (same number, different colors)
        ("{r3, o3, blue3, black3}", True),
        ("{blue1, black1, r1}", True),  # Valid group (same number, different colors)
        

        # Invalid: duplicate cards in set
        ("{r5, r5}", False),
        ("{blue2, blue2, blue3}", False),

        # Invalid: set numbers not consecutive
        ("{r1, r3}", False),
        # valid set but not in correct order
        ("{black4, black6, black5}", True),  

        # Invalid: group colors repeated
        ("{r3, r3, blue3}", False),
        ("{o2, blue2, o2}", False),

        # Invalid: neither valid set nor valid group
        ("{r1, blue2, black3}", False),

        # Invalid: invalid tile format
        ("{red1, o2}", False),  # 'red' is not a valid color
        ("{r0, o2}", False),    # number 0 invalid
        ("{r14, blue3}", False), # number 14 invalid

        # Invalid: empty set
        ("{}", False),
        ("{   }", False),

        # Multiple sets valid
        ("{r1, r2, r3}, {blue4, blue5, blue6}", True),

        # Multiple sets with one invalid
        ("{r1, r2, r4}, {blue4, blue5, blue6}", False),
        (" { r1 , r2 , r3 } ", True),                        # Extra spaces and spacing around commas
("{r1,r2,   r3}", True),                             # Irregular spacing
("{r1 r2 r3}", True),                                # Space-separated instead of commas
("{r1, r2 r3}", True),                               # Mixed comma/space
("{r1,r2,r3},{blue4 blue5 blue6}", True),            # Multiple sets, mixed format
("\t{r1, r2, r3}\n", True),                          # Tabs/newlines
("r1, r2, r3", False),                               # Missing braces
("{r1, r2, r3", False),                              # Missing closing brace
("r1, r2, r3}", False),                              # Missing opening brace
("{r1; r2; r3}", False),                             # Wrong delimiter (; instead of , or space)
("{r1 r2,}", False),                                 # Trailing comma or syntax error
("{r1,,r2}", False),                                 # Double commas
("{,r1,r2}", False),                                 # Leading comma
("{r 1, r2}", False),                                # Space inside a tile
("{R1, o2}", False),                                 # Uppercase color (if strict)
("{blue03, blue04}", False),                          # Leading zeroes (not allowed)
("{blue3.0, blue4}", False),                         # Decimal number (invalid)
("{blue-3, blue4}", False),                          # Negative number

    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        valid, message = validate_colornumber_input_board(input_str)
        result = "PASS" if valid == expected else "FAIL"
        print(f"Test {i}: {input_str} -> Expected: {expected}, Got: {valid} [{result}]")
        if valid != expected:
            print(f"  Message: {message}")

if __name__ == "__main__":
    run_tests()
