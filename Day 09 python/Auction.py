import os 
bid = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid} ")
while not bidding_finished:
    name = input("Enter Your Name :")
    price = int(input("Entre Your bid ? "))
    bid[name]=price
    should_countinue = input("Are there any other bidders? type 'yes' or 'no' :")
    if should_countinue =="no":
        bidding_finished = True
        find_highest_bidder(bid)
    elif should_countinue == "yes":
        os.system('cls')
    