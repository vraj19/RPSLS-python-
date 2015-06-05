import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
   
    if   name == "rock":     return 0
    elif name == "Spock":    return 1
    elif name == "paper":    return 2
    elif name == "lizard":   return 3
    elif name == "scissors": return 4
    else:                    return None


    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if   number == 0: return "rock"
    elif number == 1: return "Spock"
    elif number == 2: return "paper"
    elif number == 3: return "lizard"
    elif number == 4: return "scissors"
    else:             return None

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice
    
    # convert the player's choice to player_number using the function name_to_number()
    
    player_number = name_to_number(player_choice)
    
    print 'Player Chooses',player_choice

    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice
    
    comp_choice = number_to_name(comp_number)
    
    print 'Computer Chooses',number_to_name(comp_number)
     
    

    # compute difference of comp_number and player_number modulo five

    result = ( player_number - comp_number ) % 5

    # use if/elif/else to determine winner, print winner message
    
    if result == 1 or result == 2:
        winner = 'Player wins!'
    elif result == 3 or result == 4:
        winner = 'Computer wins!'
    else:
        winner = 'Player and computer tie!'

    print 'Winner',winner
    print '\n'

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


