#todo:
#    - implement help and version (see shortopts)
#    - handle unexpected command line args gracefully with exception handling

import random
import sys
from getopt import getopt
from copy import deepcopy
#debugging
#debugging = True #later make this only true when an argument in passed to the script

#help for -h flag
helpstring = 'no help written yet'
versionstring = 'no versioning implemented yet'

#OPTION HANDLING
args = sys.argv[1:]
shortopts = 'hv'
longopts = ['verbosity=']
verbosity = 0
opts = getopt(args,shortopts,longopts)
#loop through args and do things
for option,value in opts[0]:
    if option=='--verbosity':
        verbosity = int(value)
        print("verbosity level is", verbosity)
    elif option=='-h':
        print(helpstring)
        sys.exit()
    elif option=='-v':
        print(versionstring)
        sys.exit()

#globals
cardnames = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')
suits = ('hearts','diamonds','clubs','spades')

#class definitions {{{

class Card(object):
    def __init__(self, id_no, suit):
        self.id_no = id_no
        self.suit = suit

default_deck = []
for suit in suits:
    for i in range(13):
        default_deck.append(Card(i, suit))

class Player(object):
    def __init__(self,name):
        self.name = name
        # idea: maybe hand should be an object
        # subclass set, add get_hand_value function
        self.current_hand = []
        self.standing = False
        self.busted = False
        self.wins = 0
        self.draws = 0

#}}}

#Function definitions {{{

def debug_print(x, min_verbosity = 1):
    min_verbosity = int(min_verbosity)
    if verbosity >= min_verbosity:
        print()
        print(x)

#minor game tasks
def new_deck():
    return deepcopy(default_deck)

def deal_card(deck, player): 
    player.current_hand.append(deck.pop()) 
    #using pop() because it removes Card from deck

def deal(players, deck):
    #takes list of Player objects, deals them cards
    for player in players:
        deal_card(deck, player)        
        deal_card(deck, player)        

#major game control structures
def round(players):
    print("\nbeginning new round")

    #initialise deck
    round_deck = new_deck()
    random.shuffle(round_deck)
    debug_print("round_deck list created and shuffled")

    deal(players,round_deck)
    
    #this is where players will need to be able to view their cards somehow

    #while players_inthegame>0:
    #need to ensure that this looping happens in a predictable order, maybe player order
    #add Player id number member variable, created in generate_players?
    for player in players.values():
        if standorhit(player)=='h':
            deal_card(player,round_deck)
            #should we test for busted here, or in a separate loop after the decisions have been made?
        else:
            num_players_standing += 1
            player.standing = True
def game():
    PLAYER_NAMES = get_players()
    round(PLAYER_NAMES) #or something

#}}}
