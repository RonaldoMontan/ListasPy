lista = []
controle = ''



while controle in 'yY':
    lista.append(int(input("Informe o valor para adicionar: ")))
    for posição in range(len(lista)):
        print()     



    controle = str(input("Deseja continuar ? (Y/N): "))
