

def is_anagram(word1,word2):

   str_w1 = sorted(word1)

   str_w2 = sorted(word2)


   return str_w1==str_w2

print(is_anagram("cat","act"))
print(is_anagram("silent","listen"))
print(is_anagram("silents","listen"))



