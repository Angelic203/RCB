
from add import add_numbers
# Example usage
def test_add_numbers():
    assert add_numbers(5, 3), "Test case failed: 5 + 3 should be 8"
    assert add_numbers(-1, 1), "Test case failed: -1 + 1 should be 0"
    assert add_numbers(0, 0), "Test case failed: 0 + 0 should be 0"
    assert add_numbers(-5, -3), "Test case failed: -5 + -3 should be -8"
    print("All test cases passed!")