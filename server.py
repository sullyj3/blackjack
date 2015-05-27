#todo:
    #implement help and version (see shortopts)

    #handle unexpected command line args gracefully with exception handling

import random
import sys
from getopt import getopt
from copy import deepcopy
#debugging
#debugging = True #later make this only true when an argument in passed to the script

#help for -h flag
helpstring = 'no help written yet'
versionstring = 'no versioning implemented yet'

#---------option handling
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
    def __init__(self,name,current_hand):
        self.name = name
        self.current_hand = current_hand
        self.standing = False
        self.busted = False
        self.wins = 0
        self.draws = 0

    def get_current_hand_human_readable(self):
        hand = []
        for card in self.current_hand:
            #hand.append((card.name,card.suit))
            hand.append(card.name + ' of ' + card.suit)
        hand = ', '.join(hand)
        return hand
#}}}

#Function definitions {{{

def debug_print(x,min_verbosity = 1):
    min_verbosity = int(min_verbosity)
    if verbosity >= min_verbosity:
        print()
        print(x)

#minor game tasks
def deal_card(deck,player): 
    (player.current_hand).append(deck.deck_as_list.pop(0)) 
    #using pop() because it removes Card from deck
def initial_deal(players,round_deck): #takes dict of Player objects, updates current_hand attribute
    for player in players.values():
        deal_card(round_deck, player)        
        deal_card(round_deck, player)        
    for player in players.values():
        debug_print( ( player.name+" - hand:" , player.get_current_hand_human_readable() ), 2 ) 

def standorhit(player): #takes a Player object, updates player.standing attribute. returns decision
    decision = ''
    print("Will "+player.name+" (s)tand or take a (h)it?")
    #keep asking till valid input
    while not decision in ('h','s'):
        decision = input('> ').lower()
        if not decision in ('h','s'):
            print("please enter either 's' or 'h'")
    if decision=='h':
        player.standing = False
    elif decision=='s':
        player.standing = True
    return decision

#major game control structures
def round(PLAYER_NAMES):
    print("\nbeginning new round")

    #initialise player objects AS DICT
    players = generate_players(PLAYER_NAMES)
    debug_print("players initialised")
    debug_print(players,2)

    num_players_busted = 0
    num_players_standing = 0
    num_players_inthegame = len(players)-num_players_busted-num_players_standing

    #initialise deck
    round_deck = Deck()
    round_deck.shuffle()
    debug_print("round_deck list created and shuffled")

    initial_deal(players,round_deck)
    #a player's hand can't be over 21, but test for blackjacks here.
    
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
