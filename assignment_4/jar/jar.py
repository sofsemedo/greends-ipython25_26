# objetivo: criar uma classe Jar que simula um pote de cookies
# 1. Guardar cookies até uma capacidade máxima
# 2. Adicionar (deposit) cookies ao pote
# 3. Retirar (withdraw) cookies do pote
# 4. Mostrar o pote como string de emojis de cookies


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("A capacidade deve ser um inteiro não negativo.")
        self._capacity = capacity # capacidade máxima do pote
        self._size = 0            # cookies atualmente no pote

    def __str__(self):
        return "🍪" * self._size # representação visual do pote

    def deposit(self, n):     # deposit manipula cookies com segurança
        if self._size + n > self._capacity:
            raise ValueError("Não há espaço suficiente para tantos cookies.")
        self._size += n

    def withdraw(self, n):    # withdraw manipula cookies coms segurança
        if n > self._size:
            raise ValueError("Não há cookies suficientes para retirar.")
        self._size -= n

    @property               # permite aceder a atributos sem alterar diretamente
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
