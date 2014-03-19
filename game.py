#initialise deck. is this the best data structure?

cards=list(zip((["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']),([(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]))) #generates list of 2-tuples with form ("card-name",value)
print(type(cards))
print(cards)

hearts=[card[0] for card in cards]
clubs=[card[0] for card in cards]
diamonds=[card[0] for card in cards]
spades=[card[0] for card in cards]

deck={"hearts":hearts,"clubs":clubs,"diamonds":diamonds,"spades":spades}

print()
print(type(deck))
print(deck)

#initialise players

players=[]
def get_players():
    num_players=int(input("Input number of players: "))
    for i in range(num_players):
        add_player=input("Input player "+str(i+1)+" name: ")
        players.append(add_player)

get_players()
#print(players)

def initial_deal():
    pass
