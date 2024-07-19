from replit import clear

from art import logo

print(logo)

bidders = {}
bidding_finished = False

def find_highest_bidder(bidding_list):
  highest_bid = 0
  winner = ""
  for bidder in bidding_list:
    bid_amount = bidding_list[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bidders[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bidders)
  elif should_continue == "yes":
    clear()


"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. You can use use PyCharm to write your own clear() function or configure your IDE like so.

"""
