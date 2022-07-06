listatotal = []
pares = []
impares = []
value = 0
for i in range(0, 7):
    value = int(input("Informe o valor: "))

    if value %2 == 0:
        pares.append(value)
        pares = sorted(pares)

    else:
        impares.append(value)   
        impares = sorted(impares)     

listatotal.append(pares[:])
listatotal.append(impares[:])

print(listatotal)
print(f'lista pares {listatotal[0]}')
print(f'Lista Impares {listatotal[1]}')

#---Outra maneira de fazer---

lista = [[], []]

for w in range(0, 7):
    numero = int(input('digite seu valor: '))
    if numero %2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

#ordedando os valores para crescente da lista interna
lista[0].sort()
lista[1].sort()

print(f"Valores pares da lista {lista[0]}")
print(f"Valores impares da lista {lista[1]}")
