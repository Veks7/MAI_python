'''
https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/python
'''
units = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
tens = {"ten" : 10, "twenty" : 20, "thirty" : 30, "forty" : 40, "fifty" : 50, "sixty" : 60, "seventy" : 70, "eighty" : 80, "ninety" : 90}
teens = {"eleven" : 11, "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16, "seventeen" : 17, "eighteen" : 18, "nineteen" : 19}


def parse_tens_units(s):
    number = 0
    if len(s):
        s_list = s.replace('-', ' ')
        s_list = s_list.split()
        for el in tens:
            for word in s_list:
                if word == el:
                    number += tens[el]
        for el in units:
            for word in s_list:
                if word == el:
                    number += units[el]
        if not number:
            for el in teens:
                for word in s_list:
                    if word == el:
                        number += teens[el]
    return number


def parse_hundred(s):
    return units[s] * 100


def parse_thousand(s):
    number = 0
    right = s
    if "hundred" in s:
        number += parse_hundred(s[:s.find('hundred') - 1])
        right = s[s.find('hundred') + 8:]
    number += parse_tens_units(right)
    return number * 1000


def parse_int(string):
    print(string)
    number = 0
    if "zero" == string:
        return 0
    if "one million" == string:
        return 1000000
    right = string
    if "thousand" in string:
        number += parse_thousand(string[:string.find('thousand') - 1])
        right = string[string.find('thousand') + 9:]
    right_2 = right
    if "hundred" in right:
        number += parse_hundred(right[:right.find('hundred') - 1])
        right_2 = right[right.find('hundred') + 8:]
    number += parse_tens_units(right_2)
        
    return number


