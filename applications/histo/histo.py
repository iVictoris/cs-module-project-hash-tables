# Your code here
import re

def word_count(s: str):
    # Your code here
    cache = {}
    for char in '":;,.-+=/\\|[]{}()*^&':
        s = s.replace(char, '')

    s = re.sub(r'\s+', ' ', s).lower().split(' ')
    for word in s:
        try:
            cache[word] += 1
        except KeyError:
            if not word:
                continue
            cache[word] = 1
    return cache

def order_results():
    # so we need to sort each key in words
    ordered_words = {}
    for key in words:
        try:
            ordered_words[words[key]] += [key]
        except KeyError:
            ordered_words[words[key]] = [key]
    return ordered_words

with open('robin.txt') as f:
    words = word_count(f.read())
    ordered_results = order_results()

    # now that we have this, sort the keys by highest to lowest
    order = sorted(list(ordered_results.keys()))
    order.reverse()

    for count in order:
        # grab the words in ordered_words for specific key
        words_to_print = sorted(ordered_results[count])
        for word in words_to_print:
            hashes = "#" * count
            area_between_hashes = 15
            spaces = area_between_hashes - len(word)
            space_chars = " " * spaces
            print(f"{word}{space_chars}{hashes}")
