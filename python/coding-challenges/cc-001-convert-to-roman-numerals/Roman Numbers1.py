def InttoRoman2(number):
    int_roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),\
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    if not number.isdigit():
        return "Not Valid Input !!!"
    number = int(number)
    if (number > 3999) or (number < 1):
        return "Not Valid Input !!!"
    result = ""
    while number > 0:
        for i, roman in int_roman_map:
            while number >= i:
                result += roman
                number -= i
    return result

def InttoRoman2(number):
    int_roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
        return "Not Valid Input !!!"
    number = int(number)    
    result = ""
    while number > 0:
        for i, roman in int_roman_map:
            while number >= i:
                quotient = number // i 
                result += roman * quotient
                number %= i
    return result

def InttoRoman(number):
    romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
    if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
        return "Not Valid Input !!!"
    number = int(number)    
    result = ""
    for key, value in romandict.items():
        while number >= value:
            quotient = number // value 
            result += key * quotient
            number %= value
    return result
    
print("###  This program converts decimal numbers to Roman Numerals ###",'\nTo exit the program, please type "exit")')
while True:
    number = input("Please enter a number between 1 and 3999, inclusively : ")
    if number == "exit":
        print("Exiting the program... Good Bye")
        break
    print(InttoRoman(number))