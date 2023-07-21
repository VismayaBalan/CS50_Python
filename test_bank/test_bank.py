from bank import value

def main():
    test_value()

def test_value():
    assert value('Hello') == 0
    assert value('happy') == 20
    assert value('Cat') == 100
    assert value('Cat is so funny') == 100
    assert value('What’s up') == 100

if __name__ == '__main__':
    main()
