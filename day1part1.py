from typing import List
import re

def input_to_lines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")

input = input_to_lines("aocinput1-1")
sum = 0
for line in input:
    firstDigit = re.search(r'([0-9]).*', line).group(1)
    lastDigit = re.search(r'.*([0-9])', line).group(1)
    number = eval(firstDigit + lastDigit)
    sum += number
print()