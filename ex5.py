# Resolução exercício 5

"""
Para solucionar a questão, deve-se seguir os seguintes passos:

1 - Ligar o interruptor 1, esperar alguns minutos e apagá-lo
2 - Ligar o interruptor 2, esperar alguns minutos e apagá-lo.
3 - Ir até a sala A, e verificar a temperatura da lâmpada.
4 - Ir até a sala B, e verificar a temperatura da lâmpada.

As lâmpadas só poderão estar: quente, morna ou fria

Se na sala A a lâmpada estiver quente, o interruptor é o de nº 2.
Se na sala A a lâmpada estiver morna, o interruptor é o de nº 1.
Se na sala A a lâmpada estiver fria, o interruptor é o de nº 3.

Se na sala B a lâmpada estiver quente, o interruptor é o de nº 2.
Se na sala B a lâmpada estiver morna, o interruptor é o de nº 1.
Se na sala B a lâmpada estiver fria, o interruptor é o de nº 3.

Por fim, sabendo a temperatura em A e B e relacionando com os interruptores
1, 2 ou 3 (o interruptor 3 não foi ligado, logo será a lâmpada fria), saberemos
qual interruptor controla cada lâmpada.

"""