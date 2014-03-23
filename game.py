from random import randrange

class card(object):
    def __init__(self,name,face_value,suit):
        self.name=name
        self.face_value=face_value
        self.suit=suit

class player(object):
    def __init__(self,name,current_hand):
        self.name=name
        self.current_hand=current_hand

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

def shuffle_deck(deck): # takes and returns a list of cards
    temp_deck=deck
    shuffled_deck=[]

    while len(temp_deck)>0:
        random_index=randrange(len(temp_deck))
        shuffled_deck.append(temp_deck[random_index])
        del temp_deck[random_index]

    return shuffled_deck

def deal_card(deck,player): #make sure deck is shuffled before calling this
    #deck should be a list, player should be a player object
    (player.current_hand).append(deck.pop(0)) #pop() removes card from deck

deck_dict=init_deck()
deck_list=[x for x in deck_dict.values()]
main_deck=shuffle_deck(deck_list)

players=generate_players(get_players())
