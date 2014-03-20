#initialise deck. is this the best data structure?
cardnames=["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']
cardvals=[(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]
cards=list(zip(cardnames,cardvals)) #generates list of 2-tuples with form ("card-name",value)

#print(cards)

hearts,clubs,diamonds,spades={},{},{},{}

for suit in (hearts,clubs,diamonds,spades): #populates each suit with 1 of each type of card
    for card in cards:
        suit[card[0]]=card[1]

deck={"hearts":hearts,"clubs":clubs,"diamonds":diamonds,"spades":spades}
temp_deck=deck
shuffled_deck=[]

#print()
#print(type(deck))
for suit in deck:
    print(suit+str(deck[suit]))

#initialise players
#maybe should use classes instead?
players=[]

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
