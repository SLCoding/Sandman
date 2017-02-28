# source: http://doc.pytest.org/en/latest/

def inc(x):
    return x + 1

def test_good():
    assert inc(3) == 4

def test_bad():
    assert inc(3) == 5
