#Jogo de decisões

#Iniciando o jogo
print('Iniciando o jogo')

#Fase 1 - pergunta 1
print('NIVEL 1')
print('São 5h da manhã, deseja levantar da cama?')
print('[1]- Sim, já é hora de levantar. [2]- Ainda não, posso dormir mais um pouco')

resposta1 = int(input('Escolha uma opção: '))

if resposta1 == 1:
    print('Otimo, você se levantou mais cedo e agora pode se preparar seu café da manhã.')
    #Fase 1 - pergunta 2
    print('Deseja comer oque no café da manhã? ')
    print('[1] - ovos e pão. [2] - Frutas e leite.')
    resposta2 = int(input('Escolha uma opção: '))

    if resposta2 == 1:
        print('Você comeu seu pão com ovo e foi trabalhar. ')
        print('FIM DO JOGO!')
    elif resposta2 == 2:
        print('Você comeu suas frutas com leite e foi trabalhar. ')
        print('FIM DO JOGO!')

elif resposta1 == 2:
    print('OH NÃO! Você dormiu demais, precisa se arrumar rápido ou irá se atrasar. ')
    #Fase 2 - pergunta 2
    print('Deseja tomar café da manhã?')
    print('[1] - Sim, acredito que dê tempo. [2] - Melhor não, posso perder o ultimo onibus.')
    resposta3 = int(input('Escolha uma opção: '))
    if resposta3 == 1:
        print('Você comeu e perdeu o ultimo onibus.')
        print('FIM DO JOGO!')
    if resposta3 == 2:
        print('Por pouco não perde o onibus')
        print('FIM DO JOGO!')


