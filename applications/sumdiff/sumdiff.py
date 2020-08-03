"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import random
import math

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
"""
n = 4
out: 256
1111
1113
1114
1117

1131
1141
1171

1311
1411
1711

1333
1334
1337

1343
1373

1433
1733



1347
1374
1437
1473
1734
1743
3147
3174
3417
3471
3714
3741
4137
4173
4317
4371
4713
4731
7134
7143
7314
7341
7413
7431

q = (1, 3, 4, 7)

1 3 4 7
1!

q = (1, 3, 4, 7, 12)

1 3 4 12
1 3 7 12

1 4 7 12
2!

3 4 7 12
1!

2! + 1! => 4

q = (1, 3, 4, 7, 12, 15)
--- 6 --- 
1 3 4 15 
1 3 7 15
1 3 12 15

1 4 7 15
1 4 12 15

1 7 12 15
3! 6

3 4 7 15
3 4 12 15

3 7 12 15
2! 3

4 7 12 15
1! 1

n = 4 => (1) * 24=> 24 1!
n = 5 => (1 + 4) * 24=> 120 1! + 2!
n = 6 => (1 + 4 + 10) * 24 => 288 1! + 2! + 3!
n = 7 => (1 + 4 + 10 + 20) * 24 => 624 1! + 2! + 3! + 4!

q = (1, 3, 4, 7, 12, 15, 13)

---- 7 ----
1 3 4 13
1 3 7 13
1 3 12 13
1 3 15 13

1 4 7 13
1 4 12 13
1 4 15 13

1 7 12 13
1 7 15 13

1 12 15 13

3 4 7 13
3 4 12 13
3 4 15 13

3 7 12 13
3 7 15 13

3 12 15 13

4 7 12 13
4 7 15 13

4 12 15 13

7 12 15 13


q = (1, 3, 4, 7, 12, 15, 13, 8)
------- 8 ----------
1 3 4 8
1 3 7 8
1 3 12 8
1 3 15 8
1 3 13 8

1 4 7 8
1 4 12 8
1 4 15 8
1 4 13 8

1 7 12 8
1 7 15 8
1 7 13 8

1 12 15 8
1 12 13 8

1 15 13 8
5!

3 4 7 8
3 4 12 8
3 4 15 8
3 4 13 8

3 7 12 8
3 7 15 8
3 7 13 8

3 12 15 8
3 12 13 8

3 15 13 8
4!

3!

2!

1!
5! + 4! + 3! + 2! + 1!
15 + 10 + 6 + 3 + 1
"""


def f(x):
    return x * 4 + 6

# Your code here
def sumdiff(a, b, c, d):
    left = f(a) + f(b)
    right = f(c) - f(d)
    return left == right

def format_string(a, b, c, d):
    return f'f({a}) + f({b}) = f({c}) - f({d})\t{f(a)} + {f(b)} = {f(c)} - {f(d)}'
def get_possible_combinations(n, k):
    # return (math.factorial(n)//(math.factorial((n-k))*math.factorial(k))) * 256 #it's not this
    return n**k

guesses = {}
max_guess_attempts = get_possible_combinations(len(q), 4) # key to solving problem
while len(guesses) < max_guess_attempts: 
    choices = tuple(random.choices(q, k=4))
    if guesses.get(choices):
        continue
    is_equal = sumdiff(*choices)
    guesses[choices] = is_equal
# go through guesses and merge Trues and False
# didn't really need to do this but too lazy to think

valid_or_not = {}
for key, value in guesses.items():
    try:
        valid_or_not[value] += [key]
    except KeyError:
        valid_or_not[value] = [key]
    
for values in valid_or_not[True]:
    print(format_string(*values))