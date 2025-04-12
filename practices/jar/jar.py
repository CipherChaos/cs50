class Jar:
    def __init__(self, capacity=12):
        # Validated via setter
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, number):
        if number < 0:
            raise ValueError("Cannot deposit a negative number")
        if number + self.size > self.capacity:
            raise ValueError("Deposit would exceed jar capacity")
        # Uses size setter for validation
        self._size += number

    def withdraw(self, number):
        if number < 0:
            raise ValueError("Cannot withdraw a negative number")
        if number > self.size:
            raise ValueError("Cannot withdraw more than available cookies")
        self._size -= number

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be an integer")
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size cannot be negative")
        if size > self._capacity:
            raise ValueError("Size cannot exceed capacity")
        self._size = size


def main():
    jar = Jar(5)
    print(jar.capacity)

if __name__ == "__main__":
    main()
