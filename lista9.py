matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = somaTerceiraColuna = 0
maior = 0
#preenchimento
for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f"guarde seu valor aui nesta posição: [{coluna} | {linha}]  "))


#leitura
for coluna in range(0, 3):
    for linha in range(0, 3):
        
        #soma valores terceira coluna
        if (coluna == 0 and linha == 2) or (coluna == 1 and coluna ==2) or (coluna == 2 and linha == 2):
            somaTerceiraColuna += matriz[coluna][linha]
           
        #soma valores pares
        if matriz[coluna][linha] %2 == 0:
            pares += matriz[coluna][linha]

        #MAIOR VALOR DA MATRIZ
        if coluna == 0 and linha == 0:
            maior = matriz[coluna][linha]
            print(maior)
        else:
            if matriz[coluna][linha] > maior:
                maior += matriz[coluna][linha]


#impressão
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz [coluna]  [linha]:^4}]', end=" ")
    print()


print(pares)
print(somaTerceiraColuna)
print(maior)