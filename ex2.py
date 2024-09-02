palavra = input('Insira uma palavra: ')

dicionario = {}

for caracter in palavra:
    if dicionario.get(caracter):
        dicionario[caracter] = dicionario[caracter] + 1
    else:
        dicionario[caracter] = 1

print(dicionario)    
    
    




