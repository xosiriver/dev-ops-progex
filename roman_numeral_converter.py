import sys

num_to_roman = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }

roman_to_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }


def to_roman_numeral(num):
    r = ''
    keys = sorted(num_to_roman.keys(), reverse=True)

    for key in keys:
        while num >= key:
            r += num_to_roman[key]
            num -= key
    
    return r


def to_arabic_number(numeral):
    anum = 0
    for e, i in enumerate(numeral):
        if e < len(numeral) - 1:
            if roman_to_num[i] >= roman_to_num[numeral[e + 1]]:
                anum += roman_to_num[i]
            else:
                anum -= roman_to_num[i]
        else:
            anum += roman_to_num[i]
    
    return anum


if sys.argv[1].isdigit():
    print(to_roman_numeral(int(sys.argv[1])))
else:
    print(to_arabic_number(str(sys.argv[1])))
 