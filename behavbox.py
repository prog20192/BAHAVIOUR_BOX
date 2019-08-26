print('-='*10)
print('BAHAVIOUR BOX')
print('-='*10,'\n')
print('''Suas opções:
[ 0 ] Não habituado
[ 1 ] Habituação\n''')
habituacao = int(input('O animal está habituado: '))
if habituacao:
    print('\nAlguns parâmetros serão avaliados na seguinte ordem!')
    print('ETAPA 1: Aproximação da barra')
    print('ETAPA 2: Tocar na barra')
    print('ETAPA: Discriminar o som')
    print('\nETAPA 1: APROXIMAÇÃO')
    distancia = int(input('Distância do animal até a barra: '))
    if distancia <= 30:
        print('Foi liberado 0,5 ml de recompensa!')
        print('O animal passou para etapa 2')
        print('\nETAPA 2: TOCAR NA BARRA')
        barra = int(input('Quantas vezes tocou na barra: '))
        if barra >= 20:
            print('O animal passou para a etapa 3!')
            print('\nETAPA 3: Discriminação do som e barra')
