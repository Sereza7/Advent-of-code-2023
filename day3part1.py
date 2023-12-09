from typing import List
import re

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def inputToLines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")

def isGear(lineIndex, characterIndex):
    return not (input[lineIndex][characterIndex].isnumeric() or input[lineIndex][characterIndex]=='.')


def checkValidity(lineIndex, characterIndex):
    valid=False
    if lineIndex > 0:
        if characterIndex > 0:
            valid=valid or isGear(lineIndex-1,characterIndex-1)
        valid=valid or isGear(lineIndex-1,characterIndex)
        if characterIndex < max_character:
            valid=valid or isGear(lineIndex-1,characterIndex+1)
    if characterIndex > 0:
        valid=valid or isGear(lineIndex,characterIndex-1)
    if characterIndex < max_character:
        valid=valid or isGear(lineIndex,characterIndex+1)
    if lineIndex < max_line:
        if characterIndex > 0:
            valid=valid or isGear(lineIndex+1,characterIndex-1)
        valid=valid or isGear(lineIndex+1,characterIndex)
        if characterIndex < max_character:
            valid=valid or isGear(lineIndex+1,characterIndex+1)

    return valid

def scoreGroup(group, groupIsValid):
    if(group==''): return 0
    score = groupIsValid*int(group)
    return score

input = inputToLines("aocinput3-1")
total = 0
max_line = len(input)-1
max_character = len(input[0])-1

for lineIndex in range(len(input)):
    line = input[lineIndex]
    group=''
    groupIsValid=False
    for characterIndex in range(len(line)):
        character = line[characterIndex]
        if character.isnumeric():
            group = group + character
            # Check if the group is valid, based on neighbors
            groupIsValid = groupIsValid or checkValidity(lineIndex, characterIndex)
        if (not character.isnumeric()):
            #the group ended the character before, we score and reinitialize
            total += scoreGroup(group,groupIsValid)
            group = ''
            groupIsValid=False
    total += scoreGroup(group,groupIsValid)
print(total)