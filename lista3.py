
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