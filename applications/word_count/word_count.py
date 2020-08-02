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



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))