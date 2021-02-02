from replit import clear
from art import logo

print(logo)

bid_listing = {}

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bid_listing[name] = bid

more_bids = input("Are there more bidders?\nPress 'y' or 'n'")


