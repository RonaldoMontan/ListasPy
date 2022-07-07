matriz = [[0,0,0], [0,0,0], [0,0,0]] #será uma matriz 3x3

#for para preenchimento
for coluna in range(0,3):    
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f"Guarde seu valor aqui! [{coluna},{linha}] "))

#for para leitura
for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz[coluna][linha]:^5}]', end='')#  :^5 serve para centralizar o resultado
    print() #fez a primeira linha quebra para a segunda, aqui fica o efeito 3x3   
