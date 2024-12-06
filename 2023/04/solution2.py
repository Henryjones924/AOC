import re

with open ('input.txt') as file:
    data = file.readlines()

line_list = []

#Line Clean Up
for line in data:
    fix_line = line.strip('\n')
    line_list += [fix_line]
#print (line_list) 

def DoesItWin(line_list):
    scratchdeck = []
    for card in line_list:
        wins = 0
        card_list = re.split('[,|:]',str(card))
        #Get Winning Numbers    
        winning_numbers = card_list [1]
        winning_numbers = str(winning_numbers).split()
        #Get Your Numbers
        your_numbers = card_list [2]
        your_numbers = str(your_numbers).split()
        #print (your_numbers)
        card_id = (card_list[0].split())[1]

        for winning_number in winning_numbers:
            for your_number in your_numbers:
                if winning_number == your_number:
                    wins = wins + 1
        scratchdeck.append([int(card_id),wins,1])
    return (scratchdeck)

card_list = DoesItWin(line_list)
card_index = 0
total = 0
for cards in card_list:
    i = 0
    card_index = card_index + 1
    for card in range(cards[2]):
        wins = cards[1]
        plays = cards[2]
        index = card_index
        while i < wins:
            #print ("Card:"+str(cards[0])+" "+str(cards)+"- before:"+str(card_list[index+i]))
            modcard = card_list[index+i]
            modcard[2] = modcard[2]+1
            #print ("Card:"+str(cards[0])+" "+str(cards)+"- After:"+str(modcard))
            i=i+1
        i = 0
    total += int(plays)
    print ("Completed Card: "+str(cards)+" -Number of plays:"+str(plays))
print (total)








        
    


               


