#todo:
    #implement help and version (see shortopts)

    #handle unexpected command line args gracefully with exception handling

from random import randrange
import sys
from getopt import getopt
#debugging
#debugging=True #later make this only true when an argument in passed to the script

#help for -h flag
helpstring='no help written yet'
versionstring='no versioning implemented yet'

#---------option handling
args = sys.argv[1:]
shortopts = 'hv'
longopts = ['verbosity=']

verbosity = 0

opts=getopt(args,shortopts,longopts)
#loop through args and do things
for option,value in opts[0]:
    if option=='--verbosity':
        verbosity=int(value)
        print("verbosity level is", verbosity)
    elif option=='-h':
        print(helpstring)
        sys.exit()
    elif option=='-v':
        print(versionstring)
        sys.exit()

#class definitions <---------------------------
class card(object):
    def __init__(self,name,face_value,suit):
        self.name=name
        self.face_value=face_value
        self.suit=suit

class player(object):
    def __init__(self,name,current_hand):
        self.name=name
        self.current_hand=current_hand
        self.standing=False
        self.busted=False
        self.wins=0
        self.draws=0
        def get_current_hand_human_readable(self):
            hand=[]
            for card in self.current_hand:
                #hand.append((card.name,card.suit))
                hand.append(card.name + ' of ' + card.suit)
            hand=', '.join(hand)
            return hand
#--------------------------------------------->

#Function declarations <-----------------------

def debug_print(x,min_verbosity=1):
    min_verbosity=int(min_verbosity)
    if verbosity>=min_verbosity:
        print()
        print(x)
#this is stupid. this should really be a method in player
def get_hand_human_readable(player): #returns
    hand=[]
    for card in player.current_hand:
        hand.append((card.name,card.suit))
    return hand

#initialisation:
def init_deck(): #returns a dictionary of card objects with key "cardname_suit"
    cardnames=["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']
    cardvals=[(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]
    suits=['hearts','clubs','diamonds','spades']
    deck={}
    for suit in suits:
        for i in range(13):
            #deck.append(card(cardnames[i],cardvals[i],suit))
            deck[cardnames[i]+"_"+suit]=card(cardnames[i],cardvals[i],suit)
    return deck
def get_players(): #returns list of player names
    players=[]
    num_players=int(input("Input number of players: "))
    for i in range(num_players):
        add_player=input("Input player "+str(i+1)+" name: ")
        players.append(add_player)
    return players
def generate_players(name_list): #takes a list of names as strings, returns a dict of player objects with player name as key
    players={}
    for name in name_list:
        players[name]=player(name,[])
    return players

#minor game tasks
def shuffle_deck(deck): # takes and returns a list of cards
    temp_deck=deck
    shuffled_deck=[]

    while len(temp_deck)>0:
        random_index=randrange(len(temp_deck))
        shuffled_deck.append(temp_deck[random_index])
        del temp_deck[random_index]

    return shuffled_deck
def deal_card(deck,player): #deck should be a list, player should be a player object
    (player.current_hand).append(deck.pop(0)) #pop() removes card from deck
def initial_deal(players,round_deck): #takes dict of player objects, updates current_hand attribute
    for player in players.values():
        deal_card(round_deck, player)        
        deal_card(round_deck, player)        
    for player in players.values():
        debug_print(
                ( player.name+" - hand:" , player.get_current_hand_human_readable() ), 2 ) 

def standorhit(player): #takes a player object, updates player.standing attribute. returns decision
    decision=''
    print("Will "+player.name+" (s)tand or take a (h)it?")
    #keep asking till valid input
    while not decision in ('h','s'):
        decision=input('> ').lower()
        if not decision in ('h','s'):
            print("please enter either 's' or 'h'")
    if decision=='h':
        player.standing=False
    elif decision=='s':
        player.standing=True
    return decision

#major game control structures

def init_game():
    global DECK_DICT
    DECK_DICT=init_deck()
    debug_print('DECK_DICT initialised')
    debug_print(DECK_DICT,2)

    global DECK_LIST
    DECK_LIST=[card_obj for card_obj in DECK_DICT.values()]
    debug_print('DECK_LIST initialised')
    debug_print(DECK_LIST,2)

    PLAYER_NAMES=get_players()
def round():
    print("\nbeginning new round")

    #initialise player objects AS DICT
    players=generate_players(PLAYER_NAMES)
    debug_print("players initialised")
    debug_print(players,2)

    num_players_busted=0
    num_players_standing=0
    num_players_inthegame=len(players)-num_players_busted-num_players_standing

    #initialise deck
    round_deck=shuffle_deck(DECK_LIST)
    debug_print("round_deck list created and shuffled")

    initial_deal(players,round_deck)
    #a player's hand can't be over 21, but test for blackjacks here.
    
    #this is where players will need to be able to view their cards somehow

    #while players_inthegame>0:
    for player in players.values():
        if standorhit(player)=='h':
            deal_card(player,round_deck)
            #should we test for busted here, or in a separate loop after the decisions have been made?
        else:
            num_players_standing+=1
            player.standing=True
#--------------------------------------------->

#important variable assignments

#begin game
init_game()
#round()
