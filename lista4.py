lista = []
control = ''

while control in 'Yy':
    lista.append(int(input('Insert in to here your number  ')))

    control = str(input('want to continue ? '))

print(f'were typed {len(lista)} numbers')
lista.sort(reverse=True)
print(f'List from bigest to smallest {lista}')  

if 5 in lista:
    print('the value five was typed')
else:
    print('the value five was does not typed')    