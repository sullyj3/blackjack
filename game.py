cards=zip((["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']),([(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)])) #generates list of 2-tuples with form ("card-name",value)

#deck=[foo[0] for foo in cards] #seems to fuck up the for block on line 7

#print(cards)

for card in cards:
    print(card)

def initial_deal():
    pass
