todos = []
dados = []
controle = ''
maior = menor = 0

while controle in 'sS':

    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))    
    #DESCOBRINDO MAIOR E MENOR
    if len(todos) == 0:
        maior = menor = dados[1] #o primeiro valor ja será atrinuido pois o primeiro valor pode ser o menor ou o maior 
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]   
    todos.append(dados[:])#faz uma copia das informações para todos
    dados.clear()#limpa os dados para inicirar uma nova pu seja os indices vão iniciar no zero  
    controle = str(input("Deseja continuar ?"))[0]#qualquer valor diferente de Ss sai do loop

print(f'a quantidade de pessoas registradas foi {len(todos)}')

for pessoas in todos:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}] tem o maior peso de {maior}')
        #pessoas se refere ao conjunto de dados nome e peso
        #pessoas[1] se refere ao peso por isso ele compara
for pessoas in todos:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}] tem o menor peso de {menor}')
        #pessoas se refere ao conjunto de dados nome e peso
        #pessoas[1] se refere ao peso por isso ele compara
