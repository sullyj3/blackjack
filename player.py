def get_decision_info(): #inputs to be replaced
    success_prob=input("input probability of success as percentage: > %")
    payoff=input("input the potential payoff of succeeding in taking the action as a number: > ")
    cost=input("input cost of taking action as a number. ensure that the cost is the same type of unit as the potential payoff: > ")
    return (success_prob,payoff,cost)

def decide(success_prob,payoff,cost): #hmm
    expected_return=payoff*success_prob*0.01
    if expected_return>cost:
        do_the_thing=True
    else:
        do_the_thing=False
    return (do_the_thing,expected_return,expected_return-cost)

decision_info=get_decision_info()
print(decide(*decision_info))
