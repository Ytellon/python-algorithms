# É o dia da foto da turma em uma escola local e você foi o fotógrafo escolhido para tirá-las. A classe que você irá fotografar tem um número par de alunos e todos estes alunos estão usando uniformes pretos ou laranjas em iguais quantidades, ou seja, metade da turma está com uniformes pretos e metade com uniformes laranjas. Você é responsável por arranjar os alunos em duas filas para a fotografia, uma na frente na outra. Cada fila deve conter o mesmo número de alunos e deve preencher os seguintes requisitos:

# Todas as crianças usando uniformes laranjas devem estar na mesma fila.
# Todas as crianças usando uniformes pretos devem estar na mesma fila.
# Cada aluno na fila de trás deve ser estritamente mais alto que o aluno em sua frente na fila da frente.

# Você recebe dois arrays de entrada: um contendo a altura dos alunos com uniformes pretos e outro contendo a altura dos alunos com uniformes laranjas. Estes arrays sempre terão o mesmo tamanho, e cada altura (em cm) será um número inteiro positivo. 
# Escreva uma função que returne true ou false caso seja possível ou não tirar a fotografia de uma determinada turma seguindo os parâmetros estabelecidos. Você pode assumir que cada turma tem ao menos dois alunos.

# Exemplo de entrada:
# blackUniformHeights = [150, 179, 149, 152, 154]
# orangeUniformHeights = [162, 181, 151, 160, 170]

def classPhotos(blackUniformHeights, orangeUniformHeights):
    blackUniformHeights.sort()
    orangeUniformHeights.sort()
    if blackUniformHeights[0] < orangeUniformHeights[0]:
        for i in range(len(blackUniformHeights)):
            if blackUniformHeights[i] >= orangeUniformHeights[i]:
                return False
    else:
        for i in range(len(blackUniformHeights)):
            if blackUniformHeights[i] <= orangeUniformHeights[i]:
                return False
    return True