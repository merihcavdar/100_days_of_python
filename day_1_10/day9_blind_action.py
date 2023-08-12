import day9_logo
print(day9_logo.logo)

bids = {}
bidding_finished = False
highest_bidder = ["dummy", 0]
def find_the_highest(bidding_record):
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bidder[1]:
            highest_bidder[0] = bidder
            highest_bidder[1] = bidding_record[bidder]

while not bidding_finished:
    name = input("what is your name?: ")
    price = int(input("what is your bid? $"))
    bids[name] = price
    should_continue = input("are there any bidders? type 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True
    else:
        find_the_highest(bids)

print(highest_bidder)
print(f"winner is {highest_bidder[0]} and the price is {highest_bidder[1]}")


