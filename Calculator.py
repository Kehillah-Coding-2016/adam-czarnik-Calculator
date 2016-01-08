import time
import random

x = 0

while x < 1:
    print('---------')
    print('Selections:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Quit')
    print('6. Lets have some fun with a math pun')
    print('To make a selection type the corresponding number.')

    selection = input()

    if selection == '1':
        print('You selected addition. Congrats! You clearly didnt pass second grade.')
    elif selection == '2':
        print('You selected subtraction. The only reason this is here is because Mr. Kelley said I cant make the user add a negative number because I didnt put in a subtraction option. You should thank him.')
    elif selection == '3':
        print('Lets multiply! ')
    elif selection == '4':
        print('Lets take a break from all this calculating and DIVIDE a pizza!')
    elif selection == '5':
        print('Goodbye.')
        time.sleep(2)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('blastoff')
        time.sleep(1)
        print('             ___')
        print('       |     | |')
        print('      / \    | |')
        print('     |--o|===|-|')
        print('     |---|   | |')
        print('    /     \  | |')
        print('   | U     | | |')
        print('   | S     |=| |')
        print('   | A     | | |')
        print('   |_______| |_|')
        print('    |@| |@|  | |')
        print('  ___________|_|')
        x = 1
    else:
        print('You bein cray cray.')