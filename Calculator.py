import time
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#I stole the above from stackoverflow

x = 0

def print_slow(str):
    for letter in str:
        print(letter)
        time.sleep(.1)

while x < 1:
    #print(' ')
    print(' ')
    print(bcolors.OKBLUE + bcolors.UNDERLINE + 'Selections:' + bcolors.ENDC)
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Quit')
    print('6. Lets have some fun with a math pun!')
    print(' ')
    #print(' ')

    selection = input()

    if selection == '1' or 'addition' or 'add' or 'Addition' or 'Add':
        #addition
        print('You selected addition. Congrats! You clearly didnt pass second grade.')
        time.sleep(2)
        add1 = input('Enter the first number to add: ')
        add2 = input('Enter the second number to add: ')
        addtotal = int(add1) + int(add2)
        print(str(addtotal) + ' is the total.')
        time.sleep(2)
    elif selection == '2' or 'subtraction' or 'subtract' or 'Subtraction' or 'Subtract':
        #subtraction
        print('You selected subtraction. The only reason this is here is because Mr. Kelley said I cant make the user add a negative number because I didnt put in a subtraction option. You should thank him.')
        time.sleep(2)
        sub1 = input('Enter the first number to subtract: ')
        sub2 = input('Enter the second number to subtract: ')
        subtotal = int(sub1) - int(sub2)
        print(str(subtotal) + ' is the total.')
        time.sleep(2)
    elif selection == '3' or 'multiplication' or 'multiply' or 'Multiplication' or 'Multiply':
        #multiplication
        print('Lets multiply!')
        time.sleep(2)
        mul1 = input('Enter the first number to multiply: ')
        mul2 = input('Enter the second number to multiply: ')
        multotal = int(mul1) * int(mul2)
        print(str(multotal) + ' is the total.')
        time.sleep(2)
    elif selection == '4' or 'division' or 'divide' or 'Division' or 'Divide':
        #division
        print('Lets take a break from all this calculating and DIVIDE a PI!')
        time.sleep(2)
        div1 = input('Enter the first number to divide: ')
        div2 = input('Enter the second number to divide: ')
        divtotal = int(div1) + int(div2)
        print(str(divtotal))
        time.sleep(2)
    elif selection == '5' or 'quit' or 'Quit' or 'godieinahole':
        #quit
        print(bcolors.FAIL + '5' + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.FAIL + '4' + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.FAIL + '3' + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.FAIL + '2' + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.FAIL + '1' + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.FAIL + 'BLASTOFF!!!' + bcolors.ENDC)
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
    elif selection == '6' or 'math pun' or 'pun':
        #I only put in a few puns
        puns = ['Some mathematicians are reluctant to cosine a loan.', 'I was kicked out of math class for one too many infractions.', 'A mathematician that couldnt stop adding up recently went incremental.', 'I used to hate math but then I realised decimals have a point.', 'I didnt understand the math, so the teacher summed it up for me.', 'What do organic mathematicians throw into their fireplaces? Natural Logs.', 'In high school I recall having a beautiful but difficult math teacher. She was easy on the eyes and hard on the pupils!', 'Mathematicians are sum worshippers.', 'I strongly dislike the subject of math however I am partial to fractions.', 'You know what happens after you miss math class? It starts adding up.']
        print(random.choice(puns))
        time.sleep(2)
    elif selection == 'secretpun' or selection == 'secret' or selection == 'easteregg':
        print('Hey! Put on a coat. Its like 20 degrees outside.')
        time.sleep(2)
        print('Aww, someone just made snow ANGLES')
        time.sleep(2)
        x = 1
    else:
        print(bcolors.FAIL + 'Because you didnt make a correct selection, this program will self-destruct in 3 seconds.' + bcolors.ENDC)
        time.sleep(2)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        x = 1