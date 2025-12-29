# Objetivo: garantir que a classe funciona corretamente antes de ser usada

import pytest
from jar import Jar

def test_init():  # verificar se a classe Jar é inicializada corretamente
    jar = Jar()   # cria-se a intância do Jar (jar = Jar ()) e confirma-se que
    assert jar.capacity == 12 # a capacidade do pote é a esperada
    assert jar.size == 0   # o tamanho inicial do pote é 0

def test_str():  # verificar se a representação do string do pote está correta
    jar = Jar()
    jar.deposit(3) # cria-se uma instância do Jar e deposita-se alguns cookies
    assert str(jar) == "🍪🍪🍪" # confirma-se que str(jar) mostra exatamente tantos emojis quanto cookies depositados

def test_deposit(): # verificar se adicionar cookies funciona corretamente
    jar = Jar(5)
    jar.deposit(3) # cria-se instância do Jar e deposita-se alguns cookies
    assert jar.size == 3 # o atributo size reflete o numero de cookies depositados
    # depositar mais do que a capacidade deve dar erro
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw(): # verificar se retirar cookies funciona corretamente
    jar = Jar(5)
    jar.deposit(4) # cria-se uma intância Jar e deposita-se alguns cookies
    jar.withdraw(2) # retira-se alguns cookies
    assert jar.size == 2 # o atributo size reflete corretamente a quantidade restante de cookies
    # retirar mais do que existe deve dar erro
    with pytest.raises(ValueError):
        jar.withdraw(5)
