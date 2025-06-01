#Caesar Cipher left shift 2

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) - shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

def ASCII_Progress_bar(float: P)
    floored_P = int(P)
    display_P = (floored_P // 10) * 10

    bar = "[" + "+" * (display_P // 10) + "." * (10 - (display_P // 10)) + "]"
    print(f"{bar} {floored_P}%")

#Toph : BPL Mubarak
'''
Outcome	Description
N	No ball
W	Wide ball
D	Dead ball
O	Out
0-6	Runs scored
'''
def calculate_overs(T, outcomes):
    results = []
    for S in outcomes:
        legal_balls = sum(1 for c in S if c not in ['N', 'W', 'D'])
        overs = legal_balls // 6
        balls = legal_balls % 6

        result = []
        if overs > 0:
            result.append(f"{overs} OVER" if overs == 1 else f"{overs} OVERS")
        if balls > 0 or legal_balls == 0 or (overs == 0 and balls == 0):
            result.append(f"{balls} BALL" if balls == 1 else f"{balls} BALLS")

        results.append(' '.join(result))
    return results
    '''
    EG
    T = int(input())
outcomes = []
for i in range(T):
    S = input()
    outcomes.append(S)

results = calculate_overs(T, outcomes)

for res in results:
    print(res)
'''

'''
Toph: Xtra Chocolates, Determaine how many more chocolates forhad needs to buy '''
'''
X, Y = map(int, input().split())

remainder = Y % X
if remainder == 0:
    print(0)
else:
    print(X - remainder)
    '''

# Prochurok: The digit that is used the most in a number
def most_used_digit(number):
    # Convert number to string to iterate through digits
    digits = str(number)
    
    # Dictionary to count occurrences of each digit
    count = {}
    for d in digits:
        count[d] = count.get(d, 0) + 1

    # Find the digit with the highest count
    most_frequent = max(count, key=lambda k: (count[k], -int(k)))
    
    return int(most_frequent)


'''
Taka Breaker
eg: 10 tk = 5+5
'''
'''
N = int(input())

denominations = [500, 100, 50, 10, 5, 1]
notes = []

for d in denominations:
    count = N // d
    N %= d
    notes.extend([d] * count)

# Sort ascending for output
notes.sort()

print(*notes)
'''

'''
Chess Board Cell Black or white
'''

'''
A, B = map(int, input().split())

if (A + B) % 2 == 0:
    print("Black")
else:
    print("White")
'''

'''
Fibonacci nums betweeen two nums
'''
'''
L, R = map(int, input().split())

a, b = 0, 1
printed_one = False

while a <= R:
    if L <= a <= R:
        if a == 1:
            if not printed_one:
                print(a)
                printed_one = True
        else:
            print(a)
    a, b = b, a + b

    
'''

'''
#Leetcode: Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table with (len(s)+1) x (len(p)+1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # Fill the table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]  # Treat * as 0 occurrence
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[len(s)][len(p)]

'''

# Int to Roman
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym  = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""

        i = 0
        while num > 0:
            div = num // base[i]
            while div:
                result += sym[i]
                div -= 1

            num %= base[i]
            i += 1

        return result
'''
