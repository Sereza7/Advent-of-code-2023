from typing import List
import re

def input_to_lines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")

input = input_to_lines("aocinput1-1")
sum = 0
REGEX1 = r'([0-9]|one|two|three|four|five|six|seven|eight|nine).*'
REGEX2 = r'.*([0-9]|one|two|three|four|five|six|seven|eight|nine)'
NUMBER_CONVERSION={"zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}
for line in input:
    firstDigit = re.search(REGEX1, line).group(1)
    if not firstDigit.isnumeric():
        firstDigit = NUMBER_CONVERSION[firstDigit]
    lastDigit = re.search(REGEX2, line).group(1)
    if not lastDigit.isnumeric():
        lastDigit = NUMBER_CONVERSION[lastDigit]
    try:
        number = eval(firstDigit + lastDigit)
        sum += number
    except:
        print(line)
        break
print(sum)