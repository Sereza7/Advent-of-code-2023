from typing import List
import re

def input_to_lines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")

input = input_to_lines("aocinput2-1")
sum = 0
MAX_QUANTITY={"red": 12, "green": 13, "blue": 14}

for line in input:
    header, content = line.split(':')
    gameID = re.search(r'Game (\d*)',header).group(1)
    gameFailed = False
    for round in content.split(';'):
        for item in round.split(','):
            quantity, color = item.strip().split(' ')
            if MAX_QUANTITY[color]< int(quantity): gameFailed = True
    if not gameFailed: sum += int(gameID)
print(sum)