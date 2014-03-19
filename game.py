cards=zip((["ace"]+[str(i) for i in range(2,11)]+['jack','queen','king']),([(1,11)]+[i for i in range(2,11)]+[10 for i in range(3)]))
deck=[foo[0] for foo in cards]
#print(cards)
print(deck)
#print(["foo" for card in cards])
print(cards)
for card in cards:
    print(card)
#def initial_deal():
 #   pass
