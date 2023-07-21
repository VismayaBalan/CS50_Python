from numb3rs import validate
import pytest

def main():
    test_validate()

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("271.22.5.1") == False
    assert validate("27.292.567.333") == False
    assert validate("cat") == False

if __name__ == 'main':
    main()


