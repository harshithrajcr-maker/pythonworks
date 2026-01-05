
"""
def vowel_count(word):

    count =0

    for ch in word:

        if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":

            count+=1


    return count

print(vowel_count("hellooi"))
print(vowel_count("harshith"))

"""


def vowel_count(word):

    count=0

    vowel="aeiou"

    for ch in word.casefold():

        if ch in vowel :

            count+=1

    return count


