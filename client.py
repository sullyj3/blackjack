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

