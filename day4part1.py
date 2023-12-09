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
for line in input:
    header, content = line.split(':')
    cardID = re.search(r'Card\s*(\d*)',header).group(1)
    winningNumbers, chosenNumbers = content.split('|')
    winningNumbers = winningNumbers.strip().split()
    chosenNumbers = chosenNumbers.strip().split()
    if cardID == '1': print(cardID, winningNumbers, chosenNumbers)
    cardWinners = 0
    for chosenNumber in chosenNumbers:
        cardWinners += 1*(chosenNumber in winningNumbers)
    if cardWinners > 0:
        total +=2**(cardWinners-1)
print("Total :" + str(total))