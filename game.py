#initialise deck. is this the best data structure?

def init_deck():
    cardnames=["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']
    cardvals=[(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]
    suits=['hearts','clubs','diamonds','spades']
    cards=[]
    for suit in suits:
        for i in range(13):
            cards.append((cardnames[i],cardvals[i],suit))
    return cards

#initialise players
#maybe should use classes instead?
#players=[]

def get_players(): #works
    num_players=int(input("Input number of players: "))
    for i in range(num_players):
        add_player=input("Input player "+str(i+1)+" name: ")
        players.append(add_player)

#get_players()
#print(players)

def shuffle_deck():
    pass
    #test all cards are present.
        #if not, reinitialise deck
    #while len shuffled_deck!=52
        #append random card from temp deck
        #delete that card from temp deck
    #temp_deck should end up empty, shuffled_deck should end up full


def initial_deal():
    pass
