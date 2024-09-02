# Resolução de B

lista = [2,4,8,16,32,64]

primeiro_termo = lista[0]
segundo_termo = lista[1]
ultimo_termo = lista[-1]

razao = segundo_termo / primeiro_termo # Determinando a razão da sequência

enesimo_termo = ultimo_termo * razao

print(f'O próximo elemento é {int(enesimo_termo)}')
