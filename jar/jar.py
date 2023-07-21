class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return '🍪'*self._cookies

    def deposit(self, n):
        if self._cookies + n > self.capacity:
            raise ValueError
        else:
            self._cookies += n


    def withdraw(self, n):
        if self._cookies < n:
            raise ValueError
        else:
            self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

def main():
    jar = Jar(20)
    jar.deposit(9)
    jar.withdraw(3)
    print(jar)



if __name__ == "__main__":
    main()