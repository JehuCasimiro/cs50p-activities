class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be less than 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("The Jar is full")
        if n + self._size > self._capacity:
            raise ValueError("Cannot add more cookies")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Withdraw amount exceeds jar size")
        if n < 0:
            raise ValueError("Cannot withdraw that amount of cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()