import sys

def inc(x):
    return x + 1

def test_answer():
    print("Python version")
    print(sys.version)
    assert inc(3) == 4
