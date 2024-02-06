import random

    
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
user = input(f"What is your choice: {' '.join(options)}?\n").lower()
pc = random.choice(options)

def play():
    if user == pc:
        return "Both --> {}.\n\tIT'S A TIE ¯\_(ツ)_/¯".format(pc)
    if is_win(user, pc):
        return "You --> {}\tVS\t{} <-- Pc\n\tYOU WON!".format(user, pc)
    return "You --> {}\tVS\t{} <-- Pc\n\tYOU LOST :(".format(user, pc)


def is_win(my, opponent):
    if (
        (my == options[0] and opponent == options[2]) or
        (my == options[1] and opponent == options[0]) or
        (my == options[2] and opponent == options[1])
    ):
        return True
    return False


if __name__ == '__main__':
    print(play())