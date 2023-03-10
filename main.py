from customMath import *


def safe_float_input(message="") -> float:
    try:
        return float(input(message))

    except ValueError:
        print("This is not a valid Value\n")
        safe_float_input(message)

    except:
        print("Unknown error I'm not smart enough\n")
        safe_float_input(message)


# har hørt somewhere this is good practise #Dengelsk
if __name__ == '__main__':
    print('I mit program skal du nu lave 2 2D vektore og manipulere dem')

    print('Lav din først vector')
    input1 = safe_float_input('første tal: ')
    input2 = safe_float_input('andet tal: ')
    vector1 = Vec2(input1, input2)

    print(f'du har nu lavet en vector med dataen: {vector1}')

    print('din anden vector: ')
    input1 = safe_float_input('første tal: ')
    input2 = safe_float_input('andet tal: ')
    vector2 = Vec2(input1, input2)

    print(f'du har nu lavet endnu en vector med dataen: {vector2}')

    print('Type --Help nu for at få en liste over functioner')

    running = True
    while running:
        match input():
            case '--Help':
                print('--Add\nLægger de 2 vektore sammen\n\n'
                      '--Subtract\nTrækker de 2 vektore fra \n\n'
                      '--AreEqual\nTjekker om de 2 vektore er ens\n\n'
                      '--AreNEqual\nTjekker om de 2 vektore ikke er ens\n\n'
                      '--Normalize\nReducere eller øjer en vektores længde til 1\n\n'
                      '--Length\n Find længden på en vektor'
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
                          f'Vektor1.normalize() = {vector1.normalize()}\n')

                elif chosenVec == '2':
                    print(f'Vektor2 = {vector2}\n'
                          f'Vektor2.normalize() = {vector2.normalize()}\n')

                else:
                    print(f'{chosenVec} er ikke valid vektor index')

            case '--Length':
                chosenVec = input('Vælg en vektor du vil vide længden på\n'
                                  'Skriv enten 1 eller 2\n')
                if chosenVec == '1':
                    print(f'Vektor1 = {vector1}\n'
                          f'Vektor1.length() = {vector1.length()}\n')

                elif chosenVec == '2':
                    print(f'Vektor1 = {vector1}\n'
                          f'Vektor1.length() = {vector1.length()}\n')

                else:
                    print(f'{chosenVec} er ikke valid vektor index')

            case ':q':
                running = False

            # default
            case _:
                print('Du har skrevet noget forkert....')

    print('EXIT SUCCESS')
