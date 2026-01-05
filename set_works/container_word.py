
word1 = "silent"

word2 = "send"

# is_container = True

# for ch in word2:

#     if ch  not in word1:

#         is_container=False

#         break

# print(is_container)

if set(word2).issubset(set(word1)):

    print("container word")

else:

    print ("not a container word")




