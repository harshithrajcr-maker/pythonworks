
# word ="balloon"

# wc = {}

# for ch in word:

#     if ch in wc :
        
#         print(ch,"first recursive character")

#         break
#     else:
#         wc[ch]=1

#function 

def first_recursive_character(word):
    wc ={}

    for ch in word:

        if ch in wc:
            
            return ch
        
        else:
            wc[ch]=1

    return None
        
print(first_recursive_character("he llo"))
    
