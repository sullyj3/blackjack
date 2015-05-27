#initialisation:
def get_players(): #returns list of player names
    players = []
    num_players = int(input("Input number of players: "))
    for i in range(num_players):
        #add graceful error handling for invalid input
        add_player = input("Input player "+str(i+1)+" name: ")
        players.append(add_player)
    return players

def generate_players(name_list): #takes a list of names as strings, returns a dict of Player objects with player name as key
    players = {}
    for name in name_list:
        players[name] = Player(name,[])
    return players

def standorhit(player): #takes a Player object, updates player.standing attribute. returns decision
    decision = ''
    print("Will "+player.name+" (s)tand or take a (h)it?")
    #keep asking till valid input
    while not decision in ('h','s'):
        decision = input('> ').lower()
        if not decision in ('h','s'):
            print("please enter either 's' or 'h'")
    if decision=='h':
        player.standing = False
    elif decision=='s':
        player.standing = True
    return decision

