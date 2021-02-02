from replit import clear
from art import logo

print(logo)

name = input("What is your name?\n")
bid = int(input("What is your bid?\n$"))

bid_listing = {}
bid_listing[name] = bid

more_bids = input("Are there more bidders?\nPress 'y' or 'n'")

bid_final = False
while not all_bidding():
    if more_bids == 'y':
        
