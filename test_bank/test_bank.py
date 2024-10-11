from bank import value

def test_bank():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello, Newman") == 0
    assert value("how you doing?") == 20
    assert value("what's happening?") == 100
