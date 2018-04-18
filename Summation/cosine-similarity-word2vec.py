from scipy import spatial
from operator import itemgetter

dataSetI = [3, 45, 7, 2]
dataSetII = [2, 54, 13, 15]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)

dataset=[]
label=[]

count=0
for line in open("data/word2vec_embeddings.txt"):
    line=line.strip().split()
    label.append(count)
    count+=1
    #results = map(float, dataset[1])
    dataset.append(map(float, line))

count=0
for line in open("data/test-set-sentences.txt"):
    print str(count)+" "+line.strip()
    count+=1

print "\n\n"

R=[]
done=[]
for i in range(len(label)):
    for j in range(len(label)):
        if i==j or (i,j) in done or (j,i) in done:
            continue            
        result = 1 - float(spatial.distance.cosine(dataset[i],dataset[j]))
        #print (label[i]+"\t"+label[j]+"\t"+str(result))
        R.append([label[i],label[j],result])
        done.append((i,j))

R=sorted(R, key=itemgetter(2), reverse=True)

for ele in R:
    print ele
    
