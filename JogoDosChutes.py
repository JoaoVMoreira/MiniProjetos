import random
#Jogo dos chutes se reme em acertar um numero sorteado aleatoriamente

#Definindo o limite do jogo
numero_inicial = int(input('Insira o numero inicial do jogo: '))
numero_final = int(input('Insira o numero limete do jogo: '))

#Selecionando o numero sorteado aleatoriamente
numero_sorteado = random.randint(numero_inicial, numero_final)

#Chute do usuário
numero_usuario = int(input('Chute um numero: '))

#Repetição 
while not numero_usuario == numero_sorteado:
    if numero_usuario > numero_sorteado:
        print(f'O numero {numero_usuario} é maior que o numero sorteado, chute um valor menor!')
        numero_usuario = int(input('Chute um numero: '))
    elif numero_usuario < numero_sorteado:
        print(f'O numero {numero_usuario} é menor que o numero sorteado, chute um valor maior!')
        numero_usuario = int(input('Chute um numero: '))
    

print('Você acertou!!! PARABENS!!!')