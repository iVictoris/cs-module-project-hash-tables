# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from string import ascii_uppercase

def is_ignored_char(char: str):
    return char not in ascii_uppercase

def count_letters(text: str):
    char_counter = {}
    for letter in text:
        char_to_be_ignored = is_ignored_char(letter)
        if char_to_be_ignored:
            continue
        try:
            char_counter[letter] += 1
        except KeyError:
            char_counter[letter] = 1
    
    return char_counter

def flip_letter_count(dict: dict):
    new_letter_count = {}
    for (key, value) in dict.items():
        new_letter_count[value] = key
    return new_letter_count

def create_cypher_crack(frequency_list: list, letter_count: dict, frequency_cypher: list):
    cypher = {}
    for index, frequency in enumerate(frequency_list):
        cypher_letter = letter_count[frequency]
        cracked_letter = frequency_cypher[index]
        cypher[cypher_letter] = cracked_letter
    return cypher

def crack_cypher(cypher: str, decoder: dict):
    string_builder = ""
    for letter in cypher:
        try:
            string_builder += decoder[letter]
        except KeyError:
            string_builder += letter

    return string_builder

with open('ciphertext.txt') as f:
    text = f.read()
    letter_count: dict = count_letters(text)
    frequency_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    cypher_frequency = list(reversed(sorted(list(letter_count.values()))))
    letter_count = flip_letter_count(letter_count)

    cypher_crack = create_cypher_crack(cypher_frequency, letter_count, frequency_letters)
    
    decoded = crack_cypher(text, cypher_crack)
    print(decoded)

