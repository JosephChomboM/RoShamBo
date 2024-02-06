import random
from math import ceil
    
def title():
    tex ='''
    
        ██████╗  ██████╗ ███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗  ██████╗ 
        ██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔═══██╗
        ██████╔╝██║   ██║███████╗███████║███████║██╔████╔██║██████╔╝██║   ██║
        ██╔══██╗██║   ██║╚════██║██╔══██║██╔══██║██║╚██╔╝██║██╔══██╗██║   ██║
        ██║  ██║╚██████╔╝███████║██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝
        ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ 
    
    '''
    return print(tex)

title()

options = ('rock', 'paper', 'scissors')
def play():
    user = None
    while user not in options:
        user = input(f"What is your choice: {' '.join(options)}?\n").lower()
    print(type(options[0]))
    pc = random.choice(options)
    if user == pc:
        return (0, user, pc)
    if is_win(user, pc):
        return (1, user, pc)
    
    return (-1, user, pc)


def is_win(my, opponent):
    if ((my == options[0] and opponent == options[2]) or (my == options[2] and opponent == options[1]) or (my == options[1] and opponent == options[0])):
        return True
    return False

def best_of(num):
    my_wins = 0
    pc_wins = 0
    necessary_rounds = ceil(num / 2)
    
    while my_wins < necessary_rounds and pc_wins < necessary_rounds:
        result, user, pc = play()
        if result == 0:
            print("Both --> {}.\n\tIT'S A TIE ¯\_(ツ)_/¯".format(pc))
            
        elif result == 1:
            my_wins += 1
            print("You --> {}\tVS\t{} <-- Pc\n\tYOU WON!".format(user, pc))
        else:
            pc_wins += 1
            print("You --> {}\tVS\t{} <-- Pc\n\tYOU LOST :(".format(user, pc))
    
    if my_wins > pc_wins:
        print('\nYou won the Best of {}.'.format(num))        
    else:
        print('The pc won the Best of {}.'.format(num))


if __name__ == '__main__':
    best_of(3)