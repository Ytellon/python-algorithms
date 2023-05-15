''' Escreva uma função que recebe uma string não vazia e a comprima de forma a substituir as sequências de caracteres
iguais por um contador seguido do caractere em si. Por exemplom, "AAA" deve ser codificado como "3A", "AABBB" como "2A3B" e assim por diante.
Para complicarmos um pouco, a string de entrada pode contar qualquer caractere, incluindo números e caracteres especiais. E já que as strings codificadas devem ser decodificáveis, nós não podemos ingenuamente codificar um string longa simplesmente pelo número de repetições. Por exemplo "AAAAAAAAAAAA" (12 A's) não poderia ser codificado como "12A", uma vez que esta string poderia ser decodificada tanto como "AAAAAAAAAAAA" quanto "1AA". Logo, repetições de 10 ou mais caracteres devem ser codificadas como uma sequência de repetições. Por exemplo, "AAAAAAAAAAAA" poderia ser codificado como "9A3A".

Exemplo de entrada:
string = "BBBBBBBBBBBBBAACCCDD"

Exemplo de saída:
"9B4B2A3C2D"
'''


def compress_string(string):
    result = ""
    count = 1
    prev_char = string[0]

    for i in range(1, len(string)):
        if string[i] == prev_char:
            count += 1
        else:
            result += str(count) + prev_char if count < 10 else "9" + \
                prev_char + str(count-9) + prev_char
            count = 1
            prev_char = string[i]

    result += str(count) + prev_char if count < 10 else "9" + \
        prev_char + str(count-9) + prev_char

    return result


if __name__ == "__main__":
    string = "BBBBBBBBBBBBBAACCCDD"
    print(compress_string(string))





