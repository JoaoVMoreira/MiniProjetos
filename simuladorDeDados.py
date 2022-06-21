import random

# Simulador de dados com input de valores

#Recebimento dos valores
menor_numero = int((input('Insira o o menor numero de seu dado: ')))
maior_numero = int((input('Insira o maior numero de seu dado: ')))

#Sorteio a partir do valores informados

numero_sorteado = random.randint(menor_numero, maior_numero)

#Imprimindo na tela
print(f'O numero sorteado foi {numero_sorteado}')