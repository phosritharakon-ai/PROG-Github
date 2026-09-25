import math
import random

praticipants = int(input("Number of praticipants: "))
winner = int(input("Number of winner: "))

tickets = list(range(1, praticipants + 1))

sheet_need = math.ceil(praticipants / 8)
jackpot_per_win = math.floor(8888 / winner)

winning = random.sample(tickets, winner)

print(f"Ticket sheet needed: {sheet_need}")
print(f"Prize per winner: {jackpot_per_win} THB")
print(f"Winning ticket: {winning}")