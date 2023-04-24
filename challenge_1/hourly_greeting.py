# programa que pergunta a hora ao usuario e baseando-se no horario descrito, exibe a saudacao apropriada.


entrada = input('digite a hora em numeros inteiros ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Por favor, digite um horário entre 0 e 23')

except:
    print('Por favor, digite um horário entre 0 e 23')
