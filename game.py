#initialise deck. is this the best data structure?

cards=list(zip((["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']),([(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]))) #generates list of 2-tuples with form ("card-name",value)
#print(cards)

#maybe use dicts for suits?
'''hearts=[card[0] for card in cards]
clubs=[card[0] for card in cards]
diamonds=[card[0] for card in cards]
spades=[card[0] for card in cards]
'''
hearts={}
clubs={}
diamonds={}
spades={}

for suit in (hearts,clubs,diamonds,spades):
    for card in cards:
        suit[card[0]]=card[1]

deck={"hearts":hearts,"clubs":clubs,"diamonds":diamonds,"spades":spades}
temp_deck=deck
shuffled_deck=[]

#print()
#print(type(deck))
for suit in deck:
    print(deck[suit])

#initialise players
#maybe should use classes instead?
players=[]
def get_players():
    num_players=int(input("Input number of players: "))
    for i in range(num_players):
        add_player=input("Input player "+str(i+1)+" name: ")
        players.append(add_player)

get_players()
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
