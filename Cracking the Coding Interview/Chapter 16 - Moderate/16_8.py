"""
16.8 English Int
Given any integer, print an English phrase that desccribes the integer
(e.g. One Thousand, Two Hundred Thirty Four).
"""


ones = ["one", "two", "three", "four", "five", "six", "seven", "eight",
"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
"sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy",
"eighty", "ninety"]
hundreds = "Hundred"
large = ["", "Thousand", "Million", "Billion"]
negative = "Negative"

def english(num):
    """Prints English equivalent of number"""
    if num == 0:
        return "Zero"
    string = [""]
    if num < 0:
        return "Negative " + english(num * -1) # flip number to positive
    i = 0
    while num > 0:
        if num // 1000 > 0:
            string.insert(0, englishHelper(num // 1000) + large[i])
        num /= 1000
        i += 1

def englishHelper(num):
    # hundreds
    
    hundredsPlace = hundreds[num // 100 - 1]
    hundredsRemainder = num % 100
    # tens
    tensPlace = tens[hundredsRemainder // 10 - 1]
    tensRemainder = hundredsRemainder % 10
    onesPlace =
