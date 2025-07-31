bid = {}

def add_bid(name, amount) :
    if name in bid :
        bid[name] += amount
    else :
        bid[name] = amount
        
def highest_bidder() :
    highest = 0
    winner = ""
    for name, amount in bid.items() :
        if amount > highest :
            highest = amount
            winner = name
    return winner, highest

#main
print("Welcome to the secret aution program.")

go_again = True

while go_again :
    name = input("Enter your name: ")
    amount = float(input("Enter you bidding amount : $"))
    add_bid(name, amount)
    
    go_again = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    
    if go_again == "no" :
        print(f"The winner is {highest_bidder()[0]} with a bid of ${highest_bidder()[1]}")
        go_again = False
    else : 
        print("\n" *100) #clear screen 
        print("Next bidder please!")
        
