
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
r = 0
while r != 5:
    print('Escolha uma das opções abaixo')
    r = int(input('[1] - Somar\n'
                    '[2] - Multiplicar\n'
                    '[3] - Maior\n'
                    '[4] - Novos números\n'
                    '[5] - Sair do programa\n'
                    'Sua escolha:'))
    if r == 1:
        soma = n1 + n2
        print('A soma de {} com {} é {}'.format(n1,n2,soma))
    elif r == 2:
        mult = n1 * n2
        print('A multiplicação de {} com {} é {}'.format(n1, n2, mult))
    elif r == 3:
        if n1 > n2:
            print('{} é maior e {} é menor'.format(n1,n2))
        elif n2 < n1:
            print('{} é maior e {} é menor'.format(n2, n1))
        elif n1 == n2:
            print('Os números digitados são iguais')
    elif r == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro número:'))
    elif r == 5:
        print('finalizando...')
    else:
        print('Opção invalida')
print('Programa finalizado com exito, volte sempre')
