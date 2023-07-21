from plates import is_valid

def main():
    test_valid()

def test_valid():
    assert is_valid('5HELLO') ==  False
    assert is_valid('HELLO') ==  True
    assert is_valid('HELLO, WORLD') ==  False
    assert is_valid('cs50') ==  True
    assert is_valid('cs05') ==  False
    assert is_valid('.cs50') ==  False
    assert is_valid('AAA22A') ==  False
    assert is_valid('afhgkjlklgjg') ==  False
    assert is_valid('23') ==  False
    assert is_valid('A2') ==  False
    assert is_valid('cs.,32') ==  False
    assert is_valid('cs32') ==  True
    assert is_valid('cs50p') ==  False

if __name__ == '__main__':
    main()
