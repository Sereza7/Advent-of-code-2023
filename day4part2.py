from typing import List
import re

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def inputToLines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")



input = inputToLines("aocinput4-1")
total = 0
cardGains = {}
for line in input:
    header, content = line.split(':')
    cardID = int(re.search(r'Card\s*(\d*)',header).group(1))
    cardAmount = 1 + (cardGains[cardID] if cardID in cardGains.keys() else 0)
    total += cardAmount
    #content processing
    winningNumbers, chosenNumbers = content.split('|')
    winningNumbers = winningNumbers.strip().split()
    chosenNumbers = chosenNumbers.strip().split()

    cardWinners = 0 # the amount of winning numbers picked
    for chosenNumber in chosenNumbers:
        cardWinners += 1*(chosenNumber in winningNumbers)
    #we add our earnings to a table keeping track of the different cards earned
    for cardWon in range(cardID + 1, cardID + 1 + cardWinners):
        cardGains[cardWon] = (cardGains[cardWon] if cardWon in cardGains.keys() else 0) + cardAmount
print("Total :" + str(total))