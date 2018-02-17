def duplicate_encode(word):
    word = list(word.lower())
    word_list = []
    for i in word:
        if word.count(i) > 1:
            word_list.append(')')
        else:
            word_list.append('(')
    new_string = ''.join(word_list)

    return new_string