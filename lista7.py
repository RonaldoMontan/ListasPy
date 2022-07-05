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
