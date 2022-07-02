
lista = []

while len(lista) != 5:

    value = int(input('insira o valor para adicionar na lista '))
    lista.append(value)
   
    for ind in range(0, 5):    
        value = int(input('insira o valor para adicionar na lista '))
        print(len(lista))
        
        #print(lista[r])
        if value >= lista[ind]:
            lista.insert(ind, value)
            print(lista)

        elif value <= lista[ind]:
            lista.insert(ind, value)   
            print(lista)
    print(lista)           

print(lista)

#solução mais precisa foi esta

lista = []

for indice in range(0, 10):
    value = int(input('Qual valor deseja inserir ?'))

    #inserimos o primeiro valor ou o maior valor
    if indice == 0 or value > lista[-1]:
        lista.append(value)
        print(lista)

    else:
        posição_da_varredura = 0 #aqui é o segredo para a varredura das posições
        while posição_da_varredura < len(lista):
            if value <= lista[posição_da_varredura]:
                lista.insert(posição_da_varredura, value)
                print(lista)
                break #para inserir uma vez o valor
            posição_da_varredura += 1 #este incremento tem impacto na linha 13 (while)   
            
print(lista)
