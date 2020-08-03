"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import random
import math

# q = list(range(1, 10))
# q = list(range(1, 200))
q = (1, 3, 4, 7, 12)


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