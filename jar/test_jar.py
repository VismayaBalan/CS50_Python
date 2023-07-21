from jar import Jar


def test_init():
    jar = Jar(4)
    assert jar.capacity == 4
    assert jar.size == 0
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar._cookies == 4
    jar.deposit(4)
    assert jar._cookies == 8


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(4)
    assert jar._cookies == 8
    jar.withdraw(4)
    assert jar._cookies == 4