import random, sys, argparse
 
def createParser():
    parser = argparse.ArgumentParser(
        prog= 'gen_pass',
        description= '''gen_pass it lite password generator.''',
        epilog= '''Written by Dmitry Rodionov.'''
    )

    parser.add_argument('-l', '--length', default=8, type=int, help='The length of the string. Default is 8')
    parser.add_argument('-n', '--numbers', action='store_const', const=True, help='Use if need to generate a string include numbers only')
    parser.add_argument('-w', '--words', choices=['0', '1'], help='Use if you need to generate a string include letters only. 1 - upper, 0 - lower letters.')
    parser.add_argument('-m', '--mix', choices=['0', '1'], help='Just mix numbers and letters. 1 - upper and lower, 0 - only lower letters.')

    return parser


if(len(sys.argv) > 4):
    print("Too many arguments!")
    exit(1)

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])


# Только цифры
if(namespace.numbers != None):
    for i in range(namespace.length):
        print(random.randrange(0, 9, 1), end='')

# Только буквы
if(namespace.words != None):
    for i in range(namespace.length):
        i = random.randrange(97, 123, 1)

        if(namespace.words == '1'):
            print(chr(i).upper(), end='')

        else:
            print(chr(i), end='')

# Смешанный
if(namespace.mix != None):
    for i in range(namespace.length):
        check = random.randint(0, 2) # Рандомно выбираем является ли текущий эл-т буквой или цифрой

        if(check == 1): # Если текущий эл-т - буква
            i = random.randrange(97, 123, 1)

            if(namespace.mix == '1'): # Если вкл. буквы верх. и ниж. регистров
                upper_ = random.randint(0, 2)

                if(upper_ == 1):
                    print(chr(i).upper(), end='')
                
                else:
                    print(chr(i), end='')

            else: # Только ниж. регистр
                print(chr(i), end='')

        else:   # Если цифра
            print(random.randrange(0, 9, 1), end='')

print("\n")
