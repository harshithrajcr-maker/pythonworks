
def consonent(word):

    count =0

    vowel ="aeiou"

    for ch in word.casefold():


           if ch not in vowel and ch.isalpha() :

            count+=1

    return count

print(consonent("harshithrajcr"))