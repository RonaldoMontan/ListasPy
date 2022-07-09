lista = []
listaParaCopia = list()

while True:

    lista.append(str(input(">> Nome do aluno: ")))
    lista.append(float(input(">> Nota 1:  ")))
    lista.append(float(input(">> Nota 2:  ")))
    


    resposta = str(input("Deseja continuar?  "))[0]
    if resposta in 'Nn':
        break


print(lista)