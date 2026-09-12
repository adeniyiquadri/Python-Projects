from twttr import shorten
def test_vowels():
    assert shorten("abdulwaris") == "bdlwrs"
    assert shorten("apple") == "ppl"
def test_consonant():
    assert shorten("bulb") == "blb"
    assert shorten("sulk") == "slk"
def test_uppercase():
    assert shorten("ADENIYI") == "DNY"
def test_numbers():
    assert shorten("2 apples") == "2 ppls"
def test_punctuations():
    assert shorten("! apples") == "! ppls"
