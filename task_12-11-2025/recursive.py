
words =["hello","hai","hello","is"]

recursive =[]

for w in words:

    rep = words.count(w)

    if rep>1 and w not in recursive :

        recursive.append(w)

print("recursive\n",recursive)