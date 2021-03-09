import re
def uncollapse(digits):
    # redundant solution
    searchList = {"zero", "one", "two", "three", "four",
                 "five", "six", "seven", "eight", "nine"}
    
    for digit in searchList:
        for d in re.finditer(digit, digits):
            digits = digits.replace(digit, digit + " ")
            digits = re.sub(' +', ' ', digits)
    digits = digits.strip()
    return digits
