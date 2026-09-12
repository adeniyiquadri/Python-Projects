from plates import is_valid
def test_length():
    assert is_valid("A") == False
    assert is_valid("AA222") == True
def test_punctuation():
    assert is_valid("A!1234") == False
    assert is_valid("AA 22") == False
def test_zero():
    assert is_valid("AA022") == False
    assert is_valid("AA222") == True
def test_placement():
    assert is_valid("AA2A2") == False
#Writing a test for when the plates starts with a letter not an alphabet
def test_number():
    assert is_valid("22AAA") == False
def test_alphabeticalChecks():
    assert is_valid("A1222") == False