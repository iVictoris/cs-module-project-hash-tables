def no_dups(s):
    # Your code here
    # order matters so I can't do this ' '.join(set(s.split())) 
    order = {}
    s = s.split(' ')
    count = 0
    for word in s:
        try:
            order[word]
        except KeyError:
            order[word] = count
            count += 1

    words = [None] * len(order)
    for key in order:
        words[order[key]] = key

    return ' '.join(words)


    # now go through order and look for value with 0, then 1, etc




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))