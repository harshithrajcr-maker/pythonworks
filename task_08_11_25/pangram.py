
def is_pangram_text(text):

    ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

    is_pangram =True

    for al in ALPHABETS:

        if al not in text:

            is_pangram = False

            break
    return is_pangram

print(is_pangram_text("the qucik brown fox jumps over lazy dog"))
print(is_pangram_text("helllo world"))