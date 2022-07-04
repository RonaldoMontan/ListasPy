lista = ''

#lista.append(str(input('Digite sua expressão: ')))
lista = str(input('Digite sua expressão '))

n = lista.count('(')
m = lista.count(')')

if n == m :
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida')    

