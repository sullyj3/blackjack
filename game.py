from random import randrange

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
        self.hitme=False
#--------------------------------------------->

#Function declarations <-----------------------
#debugging
debugging=True #later make this only true when an argument in passed to the script
def debug_print(x):
    if debugging:
        print()
        print(x)
def get_hand(player): #returns
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
def generate_players(name_list): #takes a list of names as strings, returns a dict of player objects
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
def initial_deal(players): #takes list of player objects, updates current_hand attribute
    for player in players:
        deal_card(main_deck, players[player])        
        deal_card(main_deck, players[player])        
    for player in players:
        debug_print((player+" - hand:",get_hand(players[player])))

def standorhit(player): #takes a player object, updates attributes. returns decision
    decision=''
    while not decision in ('h','s'):
        decision=input("Will "+player.name+" (s)tand or take a (h)it?\n>").lower()
        if not decision in ('h','s'):
            print("please enter either 's' or 'h'")
    if decision=='h':
        player.hitme=True
    elif decision=='s':
        player.standing=True
    return decision

#major game control structures
def round(players,deck): #will be main function. takes list of players, deck as list
    #todo: reset object variables from last round
    players_busted=0
    players_standing=0
    players_inthegame=len(players)-players_busted-players_standing

    initial_deal(players)
    #can't be over 21, but test for blackjacks here.
    
    #while players_inthegame>0:
        for player in players:
            if standorhit(player)='h':
                deal_card(player,main_deck)
                #should we test for busted here, or in a separate loop after the decisions have been made?
            else:
                players_standing+=1
                player.standing=True
#--------------------------------------------->

#important variable assignments
deck_dict=init_deck()
debug_print('deck_dict initialised to:')
debug_print(deck_dict)

deck_list=[x for x in deck_dict.values()]
debug_print('deck_list initialised to:')
debug_print(deck_list)

main_deck=shuffle_deck(deck_list)
debug_print("main_deck list created and shuffled")
players=generate_players(get_players())
debug_print("players =")
debug_print(players)
