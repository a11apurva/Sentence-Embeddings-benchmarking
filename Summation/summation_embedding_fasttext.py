from operator import add

sentences =['how to cook vanilla biscuits ',
'my computer is not working',
'i want to bake a cake',
'I really dont like physics',
'can I get a delicious apple pie',
'fire is dangerous in kitchen',
'I need a new laptop']

sentences= [ s.split() for s in sentences]

embeddings={}
for line in open("../data/fasttext_model_cooking.txt"):
    line=line.strip().split()
    label=line[0]
    vector=map(float,line[1:])
    embeddings[label]=vector

doc_embeddings={}
for sentence in sentences:
    buckets = [0] * 300
    for word in sentence:
        if word in embeddings:
            buckets=map(add, buckets, embeddings[word])
            print "FOUND: "+word
        else:
            print "NOT FOUND: "+word
    doc_embeddings[" ".join(sentence)]= buckets


g=open("data/fasttext_embeddings.txt","w")
for key in doc_embeddings:
    g.write(key+"\n")
    line=(map(str,doc_embeddings[key]))
    line=" ".join(line)
    g.write(line+"\n")
g.close()

g=open("data/fasttext_embeddings.txt","w")
h=open("data/fasttext_sentence_embeddings.txt","w")
for key in doc_embeddings:
    line=(map(str,doc_embeddings[key]))
    line=" ".join(line)
    g.write(line+"\n")
    h.write(line+"\n")
g.close()
h.close()
    
        

