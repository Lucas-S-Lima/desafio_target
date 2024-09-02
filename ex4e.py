# Resolução de E

fibonacci = [1,1,2,3,5,8]

anterior = fibonacci[-2]
proximo = fibonacci[-1]
soma = anterior + proximo
fibonacci.append(soma)

print(f'O próximo elemento é {fibonacci[-1]}')



    