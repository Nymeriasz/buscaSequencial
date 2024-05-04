vetor = [1, 3, 5, 4, 2, 6, 8, 7, 10, 9]
valorProcurado = 4
indice = -1
for i in range(len(vetor)):
    if vetor[i] == valorProcurado:
        indice = i
        break

print(f"O valor {valorProcurado} foi encontrado no índice {indice}")
