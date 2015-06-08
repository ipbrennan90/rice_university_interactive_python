import random

def name_to_number(name):
    name_num_dict = {'rock':0, 'Spock':1, 'paper':2, 'lizard':3, 'scissors':4}
    return name_num_dict[name]

def number_to_name(number):
    num_name_dict = {0:'rock', 1:'Spock', 2:'paper', 3:'lizard', 4:'scissors'}
    return num_name_dict[number]

def rpsls(player_choice):
    print "\n"
    print "player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    print "computer chooses " + number_to_name(comp_number)
    if (player_number-comp_number)%5 == 0:
        print "Player and computer tie!"
    else:
        condition = (player_number-comp_number)%5 == 2 or (player_number-comp_number)%5 == 1
        print "Player wins!" if condition else "Computer wins!"




rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
