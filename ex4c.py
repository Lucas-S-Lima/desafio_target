lista = [0,1,4,9,16,25,36,'x']

'''
Ao analisarmos a sequencia, nota-se que temos na realidade uma 
sequência aritmetica [0,1,2,3,4,5,6], onde cada elemento está
elevado ao quadrado. Logo, temos que:
'''
x = lista[7]

# Multiplica-se o indice da lista ao quadrado para obter o próximo valor
# Se houvesse um y após x, então y = lista[8]
# ultimo_elemento = 8 ** 2 = 64

ultimo_elemento = 7 ** 2

print(f'O próximo elemento é {ultimo_elemento}')

