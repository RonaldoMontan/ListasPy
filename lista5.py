from numpy import insert


listaTotal = []
listaImpar = []
listaPar = []

controle= int(input('quantos numeros você vai adicionar ?  '))

while len(listaTotal) != controle:
    listaTotal.append(int(input('Qual vai ser o valor ?  ')))
    
for posição in range(len(listaTotal)):

    if listaTotal[posição]%2 == 0:
        listaPar.append(listaTotal[posição])
    else:
        listaImpar.append(listaTotal[posição])


print(f'Sua lista {listaTotal}')
print(f'Lista par {listaPar}')
print(f'Lista impar {listaImpar}')            