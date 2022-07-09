from random import randint
from time import sleep

jogo = []
todosJogos = []
valor = atualiza = contador = 0

quantidade = int(input('Quantos jogos você quer fazer na mega-sena?  '))

while True:    
    #para garantir que ele preenchera a lista de jogos com os 6 numeros
    while len(jogo) < 6:
        valor = randint(1, 60)
        if valor not in jogo:#não pode sortear valores iguais
            jogo.append(valor)
            jogo.sort()

    #assim que sortear os 6 numeros ele faz uma copia para todoJogos e depois limpa a lista jogos para receber os novos 6 valores
    todosJogos.append(jogo[:])
    jogo.clear()  

    #para manter a quantidade de jogos que o usuario escolheu
    atualiza += 1
    if quantidade == atualiza:
        break

#impressão dos resultados
print()
for i in range(0, len(todosJogos)):
    print(f'>> Jogo {i+1} : {todosJogos[i]}')
    sleep(0.8)
print()