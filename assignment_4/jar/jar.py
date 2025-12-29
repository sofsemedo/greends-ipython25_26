class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("A capacidade deve ser um inteiro não negativo.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Não há espaço suficiente para tantos cookies.")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Não há cookies suficientes para retirar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
