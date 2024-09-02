numero = int(input('Insira um número inteiro: '))

fibonacci = [0,1]

soma = 1

for n in fibonacci:
    anterior = fibonacci[-2]
    proximo = fibonacci[-1]
    soma = anterior + proximo
    fibonacci.append(soma)

    if numero in fibonacci:
        print(f'O número {numero} está dentro da sequência: {fibonacci}')
        break
    elif fibonacci[-1] > numero:
        print(f'O número {numero} não está dentro da sequência: {fibonacci}')
        break
