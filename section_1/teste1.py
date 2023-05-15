# escreva uma função que recebe um array não vazio de inteiros distintos e um inteiro distinto representando uma soma alvo. Se quaisquer dois números no array de entrada somam a soma alvo, a função deve retornar eles em um array, em qualquer ordem. Se nenhum dois números somam a soma alvo, a função deve retornar um array vazio. Note que a soma alvo tem que ser obtida somando dois números inteiros distintos do array; você não pode adicionar um único inteiro a ele mesmo para obter a soma alvo. Você pode assumir que no máximo um par de números somam a soma alvo.

# Exemplo de entrada:
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))