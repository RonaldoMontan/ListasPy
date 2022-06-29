lista = [] #criando lista vazia
maior = 0
menor = 0
for indice in range(0,5): #preencheno a lista
    lista.append(int(input(f'Digite o valor da posição {indice}: ')))
    
    if indice == 0:#o primeioro valor será consifderado o maior por enquanto
        maior = menor = lista[indice]
    else:#encontrando o maior e menor
        if lista[indice] > maior:
            maior = lista[indice]
        if lista[indice] < menor:
            menor = lista[indice]           

print(f'\nOs valores são {lista}')
print(f'O maior valor encontrado foi:  {max(lista)} nas posições:', end=' ') 
#enumerate auxilia trazendo posição e valor que ela contem   
for posição, valor in enumerate(lista):
    if valor == maior:#o valor maior esta direcionado na posição, por isso o print da posição
        print(f'{posição}...', end='')
print()

print(f'O menor valor encontrado foi {min(lista)} nas posições:', end=' ')
for posição, valor in enumerate(lista):
    if valor == menor:
        print(f'{posição}...', end='')