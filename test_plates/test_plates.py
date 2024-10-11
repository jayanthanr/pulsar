from plates import is_valid

def test_valid():
    assert is_valid('HELLO') == True
    assert is_valid('CS50') == True
    assert is_valid('AA') == True

def test_invalid_zero():
    assert is_valid('CS05') == False
    assert is_valid('007BO') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False
    assert is_valid('2') == False
    assert is_valid('A') == False
    assert is_valid('A02') == False

def test_less_char():
    assert is_valid('H') == False
    assert is_valid('A22A') == False
    assert is_valid('A?1') == False
    assert is_valid('2Aa2A') == False
    assert is_valid('12') == False

def test_more_char():
    assert is_valid('GOODBYE, WORLD') == False
    assert is_valid('000000') == False
    assert is_valid('A.B.0') == False
    assert is_valid('. !') == False
    assert is_valid('      ') == False
    assert is_valid('cs.#32') == False
    assert is_valid('cs50p') == False



