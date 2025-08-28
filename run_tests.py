# run_tests.py
#Add dummy
def test_add():
    assert 1 + 1 == 2

def test_subtract():
    assert 2 - 1 == 1

if __name__ == "__main__":
    print("Running tests...")
    test_add()
    test_subtract()
    print("All tests passed!")
    print("Now with auto build on seeing changes on github")
