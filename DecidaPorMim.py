import random
# Decida por mim 

#Definido possibilidades
possiveis_respostas = ['Sim', 'Não', 'Acho melhor não', 'Acho melhor sim', 'Faz oque seu coração manda', 'Não perca essa oportunidade', 'Corre! É furada']

#Pergunda do usuário
pergunta = str((input('Qual a sua pergunda? ')))

#Respondendo pergunda aleatoriamente
print(possiveis_respostas[random.randint(0, 6)])