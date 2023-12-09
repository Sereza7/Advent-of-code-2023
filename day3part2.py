from typing import List
import re

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def inputToLines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")

def isGear(lineIndex, characterIndex):
    return input[lineIndex][characterIndex] == '*'
def addGear (adjacentGears, lineIndex, characterIndex):
    if (isGear(lineIndex,characterIndex)):
        adjacentGears.append(str(lineIndex)+','+str(characterIndex))
    return

def checkGears(lineIndex, characterIndex):
    valid=False
    adjacentGears = []
    if lineIndex > 0:
        if characterIndex > 0:
            addGear(adjacentGears,lineIndex-1,characterIndex-1)
        addGear(adjacentGears,lineIndex-1,characterIndex)
        if characterIndex < max_character:
            addGear(adjacentGears,lineIndex-1,characterIndex+1)
    if characterIndex > 0:
        addGear(adjacentGears,lineIndex,characterIndex-1)
    if characterIndex < max_character:
        addGear(adjacentGears,lineIndex,characterIndex+1)
    if lineIndex < max_line:
        if characterIndex > 0:
            addGear(adjacentGears,lineIndex+1,characterIndex-1)
        addGear(adjacentGears,lineIndex+1,characterIndex)
        if characterIndex < max_character:
            addGear(adjacentGears,lineIndex+1,characterIndex+1)
    return adjacentGears

def scoreGroup(group):
    if(group==''): return 0
    score = int(group)
    return score

input = inputToLines("aocinput3-1")
total = 0
max_line = len(input)-1
max_character = len(input[0])-1
gears = {}
for lineIndex in range(len(input)):
    line = input[lineIndex]
    group=''
    adjacentGears = []
    for characterIndex in range(len(line)):
        character = line[characterIndex]
        if character.isnumeric():
            group = group + character
            # Check the gears next to this group
            adjacentGears = adjacentGears + checkGears(lineIndex, characterIndex)
        else:
            #the group ended the character before, we score and reinitialize
            score = scoreGroup(group)
            if score>0:
                #remove duplicates
                adjacentGears = list(dict.fromkeys(adjacentGears))
                #update the gear
                for gear in adjacentGears:
                    if gear in gears.keys():
                        gears[gear] = [score] + gears[gear]
                    else: gears[gear] = [score]
            group = ''
            adjacentGears = []
    score = scoreGroup(group)
    if score>0:
        #remove duplicates
        adjacentGears = list(dict.fromkeys(adjacentGears))
        #update the gear
        for gear in adjacentGears:
            if gear in gears.keys():
                gears[gear] = [score] + gears[gear]
            else: gears[gear] = [score]
print(gears)
for scoreList in gears.values():
    if len(scoreList) == 2:
        total += scoreList[0]*scoreList[1]
print(total)