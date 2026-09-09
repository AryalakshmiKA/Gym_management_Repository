import random
ticket_list = []
while len(ticket_list) < 100:
    ticket = random.randrange(1000, 99999)
    if ticket not in ticket_list:
        ticket_list.append(ticket)

print("Total ticket generated : ",ticket_list)

winner = random.sample(ticket_list,2)
print("The 2 Lucky winner tickets are : ",winner)
