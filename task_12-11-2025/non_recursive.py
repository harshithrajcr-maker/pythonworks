
words = ["hello","hai","hello","is"]

non_recursive = []

for w in words:

    rep = words.count(w)

    if rep<2 :

        non_recursive.append(w)

print("non recursive\n",non_recursive)