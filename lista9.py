matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = somaTerceiraColuna = 0
maior = 0

#preenchimento
for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f"guarde seu valor aui nesta posição: [{coluna} | {linha}]  "))

#leitura
for linha in matriz:#vamos passando linha por linha e a coluna 2 esta fixado abaixo
    somaTerceiraColuna += linha[2]# aqui se refere aos indices [0][2] - [1][2] - [2][2] ou seja linha é o valor que varia

    for coluna in linha:#o primeiro for vai passado pela linha e este segundo passando pela coluna, com isso percorre todas as posições
        if coluna %2 == 0:
            pares += coluna

#impressão
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz [coluna]  [linha]:^4}]', end=" ")
    print()


print(f'A soma de todos os valores pares da matriz é   {pares}')
print(f'A Soma da terceira coluna é   {somaTerceiraColuna}')
print(f'O maio valor da segunda linha é   {max(matriz[1])}') 