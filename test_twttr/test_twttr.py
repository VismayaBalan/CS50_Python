from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten('hello') =='hll'
    assert shorten('HELLO') =='HLL'
    assert shorten('CS50') =='CS50'
    assert shorten('%^%&') =='%^%&'
    assert shorten('-_@Cat') =='-_@Ct'
    assert shorten('HELLO, WORLD') =='HLL, WRLD'


if __name__ == '__main__':
    main()
