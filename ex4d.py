# Resolução de D

"""
Ao analisarmos a sequência, percebe-se que ela se desenvolve como uma
progressão aritmética ao quadrado, isto é, lista = [2,4,6,8,'x'], em que cada
elemento da lista[i] é elevado ao quadrado. Logo:
"""

lista = [4,16,36,64,'x']

penultimo_elemento = lista[-2]

raiz_do_penultimo = penultimo_elemento ** (1/2) 

ultimo_elemento = int(raiz_do_penultimo + 2) ** 2

print(ultimo_elemento)
