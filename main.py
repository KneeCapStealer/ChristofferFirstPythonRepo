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

    print('Type --Help nu for at få en liste over functioner')

    while True:
        match input():
            case '--Help':
                print('--Add\nlægger de 2 vektore sammen\n\n'
                      '--Subtract\ntrækker de 2 vektore fra \n\n'
                      '--AreEqual\ntjækker om de 2 vektore er ens\n\n'
                      '--AreNEqual\ntjækker om de 2 vektore ikke er ens\n\n'
                      '--Normalize\nreducere eller øjer en vektors længde til 1\n\n'
                      'Hvordan lukker man programmet? Do you know how to exit vim?\n')

            case '--Add':
                print(f'vektor1 : {vector1}, vektor2: {vector2}\n'
                      f'vector1 + vector2 = {vector1 + vector2}')

            case '--Subtract':
                print(f'vektor1 : {vector1}, vektor2: {vector2}\n'
                      f'vector1 - vector2 = {vector1 - vector2}')

            case '--AreEqual':
                print(f'vektor1 : {vector1}, vektor2: {vector2}\n'
                      f'vector1 == vector2 # {vector1 == vector2}')

            case '--AreNEqual':
                print(f'vektor1 : {vector1}, vektor2: {vector2}\n'
                      f'vector1 != vector2 # {vector1 != vector2}')

            case '--Normalize':
                chosenVec = input('Vælg en vektor der skal normaliseres \n'
                                  'Skriv enten 1 eller 2\n')
                if chosenVec == '1':
                    print(f'Vektor1 = {vector1}\n'
                          f'Vektor1.Normalize = {vector1.normalize()}\n')

                elif chosenVec == '2':
                    print(f'Vektor1 = {vector1}\n'
                          f'Vektor1.Normalize = {vector1.normalize()}\n')

                else:
                    print('Ikke valid vektor index')

            case ':q':
                break

            case _:
                print('Du har skrevet noget forkert....')

    print('EXIT SUCCESS')
