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
cardnames = ('ace','2','3','4','5','6','7','8','9','10','jack','queen','king')
#ace face value is dealt with separately
cardvalues = ('ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
suits = ('hearts','diamonds','clubs','spades')

#class definitions {{{

class Card(object):
    def __init__(self, id_no, suit):
        if not id_no in range(13):
            raise ValueError

        self.id_no = id_no
        self.suit = suit

    def name(self):
        return cardnames[self.id_no]
    
    def value(self):
        return cardvalues[self.id_no]

    def __repr__(self):
        return "{0} of {1}".format(self.name(), self.suit)

default_deck = []
for suit in suits:
    for i in range(13):
        default_deck.append(Card(i, suit))

class Hand(set):
    def add(self, elem):
        if type(elem) is Card:
            super().add(elem)
        else:
            raise TypeError('Hands contain cards, not {}'.format(type(elem)))

    def value(self):
        #first check for blackjack
        if len(self) == 2:
            vals = {card.value() for card in self}
            if vals == {'ace', 10}:
                return 'blackjack'

        #separate cards based on whether they're aces
        aces = set()
        non_aces = set()
        for card in self:
            if card.name() == 'ace':
                aces.add(card)
            else:
                non_aces.add(card)

        # sum card values
        total = 0
        # compute sum of non ace cards
        for card in non_aces:
            total += card.value()
            if total>21:
                return 'bust'
        # now add aces
        for card in aces:
            total += 1
            if total>21:
                return 'bust'
        # convert aces from 1 to 11 if safe to do so
        for card in aces:
            if total+10 <= 21:
                total += 10
            else:
                break

        return total

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = Hand()
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
    player.hand.add(deck.pop()) 
    #using pop() because it removes Card from deck

def deal(players, deck):
    #takes list of Player objects, deals them cards
    for player in players:
        for i in range(2):
            deal_card(deck, player)        

def wait_for_decision():
    pass

#major game control structures
def round(dealer, players):
    print("\nbeginning new round")

    result = { player.name:None for player in players }

    #initialise deck
    round_deck = new_deck()
    random.shuffle(round_deck)
    debug_print("round_deck list created and shuffled")
    # deal to dealer and players
    deal((dealer, ) + players, round_deck)

    # case 1: dealer has blackjack
    if dealer.hand.value() == 'blackjack':
        for player in players:
            hand_val = player.hand.value()
            if hand_val == 'blackjack':
                result[player.name] = 'push'
            else:
                result[player.name] = 'loss'
                pass
        return result

    # case 2: dealer doesn't have blackjack
    # keep track of who's still playing
    in_round = copy(players)
    standing = []
    # check players for blackjack
    for player in players:
        hand_val = player.hand.value()
        if hand_val == 'blackjack':
            result[player.name] = 'win'
            in_round.remove(player)

    while in_round:
        #TODO: how do i wait for input in parallel?
        for player in in_round:
            #get input from player: hit or stand?
            decision = wait_for_decision()

            if decision == 'stand':
                in_round.remove(player)
                standing.append(player)
            elif decision == 'hit':
                deal_card(round_deck, player)
                hand_val = player.hand.value()
                if hand_val == 'bust':
                    result[player.name] = 'loss'
                    in_round.remove(player)
                elif hand_val == 21:
                    in_round.remove(player)
                    standing.append(player)
            else:
                raise ValueError

        # TODO: up to here. dealer should make decision here.
        ''' how should I handle the dealer?
        - Should they be a subclass of Player?
        - Do we want players to be able to be dealers?
        - Should the server be the dealer?
        '''


    return result

def game():
    PLAYER_NAMES = get_players()
    round(PLAYER_NAMES) #or something

#}}}
