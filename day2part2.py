from typing import List
import re

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

input = input_as_lines("aocinput2-1")
sum = 0

for line in input:
    header, content = line.split(':')
    gameID = re.search(r'Game (\d*)',header).group(1)
    gameQuantities={"red": 0, "green": 0, "blue": 0}
    for round in content.split(';'):
        for item in round.split(','):
            quantity, color = item.strip().split(' ')
            gameQuantities[color]=max(gameQuantities[color],int(quantity))
    power = gameQuantities["red"]*gameQuantities["green"]*gameQuantities["blue"]
    sum+=power
print(sum)