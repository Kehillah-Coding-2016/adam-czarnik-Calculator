import time
import random

x = 0

def print_slow(str):
    for letter in str:
        print(letter)
        time.sleep(.1)

while x < 1:
    print('-------------------------------------------')
    print('Selections:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Lets have some fun with a math pun')
    print('0. Quit')
    print('To make a selection type the corresponding number.')

    selection = input()

    if selection == '1':
        #addition
        print('You selected addition. Congrats! You clearly didnt pass second grade.')
    elif selection == '2':
        #subtraction
        print('You selected subtraction. The only reason this is here is because Mr. Kelley said I cant make the user add a negative number because I didnt put in a subtraction option. You should thank him.')
    elif selection == '3':
        #multiplication
        print('Lets multiply!')
    elif selection == '4':
        #division
        print('Lets take a break from all this calculating and DIVIDE a PI!')
    elif selection == '0':
        #quit
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
    elif selection == '5':
        #I only put in a few puns
        puns = ['Some mathematicians are reluctant to cosine a loan.', 'I was kicked out of math class for one too many infractions.', 'A mathematician that couldnt stop adding up recently went incremental.', 'I used to hate math but then I realised decimals have a point.', 'I didnt understand the math, so the teacher summed it up for me.', 'What do organic mathematicians throw into their fireplaces? Natural Logs.', 'In high school I recall having a beautiful but difficult math teacher. She was easy on the eyes and hard on the pupils!', 'Mathematicians are sum worshippers.', 'I strongly dislike the subject of math however I am partial to fractions.', 'You know what happens after you miss math class? It starts adding up.']
        print(random.choice(puns))
    elif selection == 'thisisasecret':
        print('[insert secret selection here]')
        x = 1
    elif selection == 'secretpun':
        print('Hey! Put on a coat. Its like 20 degrees outside.')
        time.sleep(4)
        print('Aww, someone just made snow ANGLES')
        time.sleep(4)
        x = 1
    else:
        print('Because you didnt make a correct selection, this program will self-destruct in 3 seconds.')
        time.sleep(4)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        x = 1