
g=open("cooking-corpus.txt","w")

for line in open("cooking.preprocessed.txt"):
    line2=[]
    line=line.split()
    for word in line:
        if "__label__" in word:
            continue
        line2.append(word)
    g.write(" ".join(line2)+"\n")








