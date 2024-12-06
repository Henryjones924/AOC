import re

with open ('input.txt') as file:
    data = file.readlines()

line_list = []

#Line Clean Up
for line in data:
    fix_line = line.strip('\n')
    line_list += [fix_line]
#print (line_list) 

card_wins = 0
total_points = 0
for card in line_list:
    card_list = re.split('[,|:]',str(card))
    #Get Winning Numbers    
    winning_numbers = card_list [1]
    winning_numbers = str(winning_numbers).split()
    #Get Your Numbers
    your_numbers = card_list [2]
    your_numbers = str(your_numbers).split()
    #print (your_numbers)
    for winning_number in winning_numbers:
        for your_number in your_numbers:
            if winning_number == your_number:
               if card_wins == 0: #Logic for first win
                    card_wins += 1
               else:
                   card_wins=(card_wins*2)
            else:
                pass
    total_points += card_wins
    card_wins = 0
print (total_points)

