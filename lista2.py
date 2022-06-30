lista = []

control = ''
length = 0

while control in 'yY':

    add = int(input("enter any values: "))
    if add not in lista:
        lista.append(add)  
    else:        
        print(f'Sorry, the value {add} already exists in the list' )
            
    control = str(input("want to continue ? [Y/N] "))
    length += 1
print(lista)  