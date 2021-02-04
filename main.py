from replit import clear
from art import logo
print(logo)

bid_dict = {}
bidding_finished = False
winner = ""

def bid_winner(new_bids = bid_dict):
    highest_bid = 0
    for bidder in new_bids:
        bid_amount = new_bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder.title()
    print(f"The winner is {winner} with a bid of ${highest_bid}.")



while not bidding_finished:
    name = input("What's your name?\n\t")
    bid = int(input("What's you bid?\n\t$"))
    bid_dict[name] = bid
    more_bids = input("Are there more bidders? Type 'yes' or 'no'\n\t")
    if more_bids == 'no':
        bidding_finished = True
        bid_winner(new_bids = bid_dict)
    elif more_bids == 'yes':
        clear()