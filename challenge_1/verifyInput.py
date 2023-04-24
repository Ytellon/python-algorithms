# programa que peca ao usuario para digitar um numero inteiro, informe se este numero e par ou impar.
# Caso o usuario nao digite um numero inteiro, informe que nao e um numero inteiro.


entrada = input('digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

        print (f'O numero {entrada_int} é {par_impar_texto}')

else:
    print('Isso não é um numero inteiro')

