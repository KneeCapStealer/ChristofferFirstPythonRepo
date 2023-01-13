from customMath import *

#har hørt somewhere this is good practise Dengelsk :+1:
if __name__ == '__main__':
    print('I mit program skal du nu lave 2 2D vektore og manipulere dem')
    print('Lav din først vector')
    input1 = float(input('første tal: '))
    input2 = float(input('andet tal: '))
    vector1 = Vec2(input1, input2)

    print(f'du har nu lavet en vector med dataen: {vector1}')

    print('din anden vector: ')
    input1 = float(input('første tal: '))
    input2 = float(input('andet tal: '))
    vector2 = Vec2(input1, input2)

    print(f'du har nu lavet endnu en vector med dataen: {vector2}')

    funkToCall = input('Vil du plusse eller minus de 2 vektore sammen?')

    if funkToCall == '+':
        print(f'{vector1} + {vector2} = {vector1 + vector2}')

    if funkToCall == '-':
        print(f'{vector1} - {vector2} = {vector1 - vector2}')


    normIndex = input('Jeg nåede kun at add 1 funktion mere uden atle som hedder normalize, Hvilken vector vil du prøve at normalize?\nskriv 1 eller 2')

    if normIndex == '1':
        print(f'Resultet er: {vector1.normalize()}')

    if normIndex == '2':
        print(f'Resultet er: {vector1.normalize()}')

    print('Nu havde vi ikke mere tid bye bye :+1:')