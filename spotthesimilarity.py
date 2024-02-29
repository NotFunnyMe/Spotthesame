import string
import random
symbols = []
symbols = list(string.ascii_letters)
card1 = [0]*5   #2 cards from which we have to spot similarity
card2 = [0]*5
pos1 = random.randint(0,4) 
pos2 = random.randint(0,4)
#pos1 and pos2 are same symbol positions in card1 and card2 respectively
print(pos1)
print(pos2)
samesymbol = random.choice(symbols) #taking random symbol from symbols list
symbols.remove(samesymbol) #removing that symbol from symbols list
if(pos1 == pos2):   #if both positions are same
    card2[pos1] = samesymbol #assigning same symbol to both positions
    card1[pos1] = samesymbol
else:
    card1[pos1] = samesymbol #assigning same symbol to different positions
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbols) #assigning random symbol to different positions
    symbols.remove(card1[pos2]) #removing that symbol from symbols list
    card2[pos1] = random.choice(symbols) #assigning random symbol to different positions
    symbols.remove(card2[pos1]) #removing that symbol from symbols list
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i=i+1
print(card1)
print(card2)
ch = input("Spot the similar symbol: ")
if(ch == samesymbol):
    print("Right")
else:
    print("Wrong")