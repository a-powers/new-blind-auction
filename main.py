from replit import clear
from art import logo
print(logo)

bid_dict = {}
bidding_finished = False
winner = ""

def bid_winner(new_bids = bid_dict):
    highest_bid = 0
    for bidder in new_bids:
        winner = new_bids[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
    print(f"The winner is {winner} with a bid of {highest_bid}.")



while not bidding_finished:
    name = input("What's your name?\n")
    bid = int(input("What's you bid?\n$"))
    bid_dict[name] = bid
    more_bids = input("Are there more bidders? Type 'yes' or 'no'\n")
    if more_bids == 'no':
        bidding_finished = True
        bid_winner(new_bids = bid_dict)
    elif more_bids == 'yes':
        clear()