from random import randint
from time import sleep


print('Brinque com o computador sobre adivinhar numeros!!')

num = int(input('Digite um numero e veja se ele e igual ao do computador: '))

print('PENSANDO...')
sleep(5)
pc = randint(0,9)

if num == pc:
    print(f'Voce acertou!!! Voce digitou {num} que o mesmo numero {pc} que o computador pensou!!')
    
else:
    print(f'Voce errou!! Voce digitou {num} e o numero do computador era {pc}')
    