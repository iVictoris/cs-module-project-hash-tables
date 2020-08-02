import random
import re
from string import ascii_uppercase

markov_dict = {}

def create_dict(words: str, ):
    words = re.sub(r'\s+', ' ', words).split(' ')
    for index, word in enumerate(words):
        if index + 1 >= len(words):
            break
        current_word = words[index]
        next_word = words[index + 1]
        try:
            markov_dict[current_word] += [next_word]
        except KeyError:
            markov_dict[current_word] = [next_word]


def get_start_word():
    # rules for start word
        # 1. word begins with capital letter
        # 2. starts with " followed by capital letter
    choices = list(markov_dict.keys())
    while True:
        start_word: str = random.choice(choices)
        if start_word in ascii_uppercase or start_word.startswith('"') and start_word[1] in ascii_uppercase:
            return start_word
        # This could potentially become an infinite loop if the if condition is not satisfied
    # could use recursion but that would increase space complexity

def see_if_stop_word(word: str):
    # rules for stop word:
    # 1. word ends in '.?!' or any of those followed by a "
    stop_chars = '.?!'
    return word.endswith(tuple(stop_chars)) or word.endswith('"') and word[-2] in stop_chars

def get_following_word(word):
    # so given the word
    # look in dict for value of key
    # value should be a list of values
    # should chooose a random word
    # check if that word is a stop word
    # otherwise get another word
    following_word = random.choice(markov_dict[word])

    is_stop_word = see_if_stop_word(following_word)

    if is_stop_word:
        return [following_word]
    
    return [following_word] + get_following_word(following_word)


def create_sentence():
    start_word = get_start_word()
    sentence = [start_word] + get_following_word(start_word)
    return " ".join(sentence)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # words = 'Somewhere over the rainbow Somewhere rainbow over rainbow'
    create_dict(words)
    start_word = get_start_word()
    sentence = [start_word] + get_following_word(start_word)

# TODO: analyze which words can follow other words
# Your code here 

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    sentence = create_sentence()
    print(sentence)
