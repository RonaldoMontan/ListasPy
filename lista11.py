lista = []
listaParaCopia = list()

while True:
    listaParaCopia.append(str(input(">> Nome do aluno: ")))
    listaParaCopia.append(float(input(">> Nota 1:  ")))
    listaParaCopia.append(float(input(">> Nota 2:  ")))
    listaParaCopia.append((listaParaCopia[1] + listaParaCopia[2])/2)#armazena a media na posição 3
    lista.append(listaParaCopia[:])#momento para copia das informações
    listaParaCopia.clear()#esvazia a lista para receber novos dados

    #controle do loop
    resposta = str(input("Deseja continuar?  "))[0]
    if resposta in 'Nn':
        break
print()
print('>>> Saida das informações <<<')
print('_____________________________')
print('Nº     Nome             Media')

for i in range(0, len(lista)):
    print(f'{i:<4}--  {lista[i][0]:<10} {lista[i][3]:>8.1f} ')

while True: 
    resposta = int(input('Digite o numero do aluno para ver mais detalhes ou 999 para sair: '))

    for i in range(0, len(lista)):
        if resposta == i:
            print(f'O(A) aluno(a) {lista[resposta][0]} teve   {lista[resposta][1]}  |  {lista[resposta][2]}')
            print()    
    if resposta == 999:
        break
    
print('Saindo...')    