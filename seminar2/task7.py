# правильное решение с гитхаба (https://github.com/ChaeWonKong/algorithm-with-python/blob/master/codewars/roman_numerals_encoder.py)

# romans = \
#         {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", \
#         40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", \
#         500: "D", 900: "CM", 1000: "M"}

# def solution(n):
#     romans = \
#         {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", \
#         40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", \
#         500: "D", 900: "CM", 1000: "M"}
#     keys = list(romans.keys())
#     keys.reverse()

#     def calc(n, ret):
#         for div in keys:
#             while n >= div:
#                 n -= div
#                 ret.append(div)
#         return ret
    
#     def encode(arr):
#         ret = ""
#         for num in arr:
#             ret += romans[num]
#         return ret
    
#     return encode(calc(n, []))

# print(solution(2543))

# правильное решение с codewars (https://www.codewars.com/kata/51b62bf6a9c58071c600001b/solutions/python)
def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution(2543))