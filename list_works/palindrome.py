
# words = ["cat","act","malayalam","madam"]

# palindrome_list = []

# for w in words:

#     if w == w[::-1]:

#         palindrome_list.append(w)

# print(palindrome_list)


def palindrome_words(words):

    p_words = []

    for w in words:

        if w == w[::-1]:

            p_words.append(w)
            
    return p_words

words = ["cat","act","malayalam","madam"]

print(palindrome_words(words))