#todo:
    #URGENT: restructure all functions relating to deck to take and return deck instances
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
class deck(object):
    def __init__(self):
        cardnames=["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']
        cardvals=[(1,11)]+[i for i in range(2,11)]+[10,10,10]
        suits=['hearts','clubs','diamonds','spades']

        deck={}

        for suit in suits:
            for i in range(13):
                deck[cardnames[i]+"_"+suit]=card(cardnames[i],cardvals[i],suit)

        self.deck_as_dict=deck #dictionary of card objects with key "cardname_suit" 
        #list is ordered. important for dealing
        self.deck_as_list=[ card_obj for card_obj in self.deck_as_dict.values() ] 
        
        debug_print('new deck initialised')
    def shuffle(self):
        temp_list=self.deck_as_list
        shuffled_list=[]

        while len(temp_list)>0:
            random_index=randrange(len(temp_list))
            shuffled_list.append(temp_list[random_index])
            del temp_list[random_index]
        self.deck_as_list=shuffled_list

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
def get_players(): #returns list of player names
    players=[]
    num_players=int(input("Input number of players: "))
    for i in range(num_players):
        #add graceful error handling for invalid input
        add_player=input("Input player "+str(i+1)+" name: ")
        players.append(add_player)
    return players
def generate_players(name_list): #takes a list of names as strings, returns a dict of player objects with player name as key
    players={}
    for name in name_list:
        players[name]=player(name,[])
    return players

#minor game tasks
def deal_card(deck,player): 
    (player.current_hand).append(deck.deck_as_list.pop(0)) 
    #using pop() because it removes card from deck
def initial_deal(players,round_deck): #takes dict of player objects, updates current_hand attribute
    for player in players.values():
        deal_card(round_deck, player)        
        deal_card(round_deck, player)        
    for player in players.values():
        debug_print( ( player.name+" - hand:" , player.get_current_hand_human_readable() ), 2 ) 

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
def round(PLAYER_NAMES):
    print("\nbeginning new round")

    #initialise player objects AS DICT
    players=generate_players(PLAYER_NAMES)
    debug_print("players initialised")
    debug_print(players,2)

    num_players_busted=0
    num_players_standing=0
    num_players_inthegame=len(players)-num_players_busted-num_players_standing

    #initialise deck
    round_deck=deck()
    round_deck.shuffle()
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
def game():
    PLAYER_NAMES=get_players()
    round(PLAYER_NAMES) #or something
#--------------------------------------------->
