from random import randrange

'''
def init_deck():  #initialise deck. returns list of 3-tuples of form: (name,face value,suit)
    #is this the best data structure?
    cardnames=["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']
    cardvals=[(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]
    suits=['hearts','clubs','diamonds','spades']
    deck=[]
    for suit in suits:
        for i in range(13):
            deck.append((cardnames[i],cardvals[i],suit))
    return deck
'''

class card(object):
    def __init__(self,name,face_value,suit):
        self.name=name
        self.face_value=face_value
        self.suit=suit

def init_deck():
    cardnames=["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']
    cardvals=[(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]
    suits=['hearts','clubs','diamonds','spades']
    deck=[]
    for suit in suits:
        for i in range(13):
            deck.append(card(cardnames[i],cardvals[i],suit))
    return deck

def get_players(): #maybe should use classes instead?
    players=[]
    num_players=int(input("Input number of players: "))
    for i in range(num_players):
        add_player=input("Input player "+str(i+1)+" name: ")
        players.append(add_player)
    return players

def shuffle_deck(deck):
    temp_deck=deck
    shuffled_deck=[]

    while len(temp_deck)>0:
        random_index=randrange(len(temp_deck))
        shuffled_deck.append(temp_deck[random_index])
        del temp_deck[random_index]

    return shuffled_deck

def initial_deal():
    pass

main_deck_state=shuffle_deck(init_deck())
print(main_deck_state)
