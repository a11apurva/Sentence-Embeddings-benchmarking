import tarfile
import urllib2
import os

proxy = 'http://anubhav.apurva%40hpe.com:Wayneroony%4010@web-proxy.atl.hp.com:8088'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

'''Download'''

print("Downloading...")

destDir="corpus"
os.mkdir(destDir)

fileName="cooking_corpus.zip"
filePath=os.path.join(destDir,fileName)

url = 'https://s3-us-west-1.amazonaws.com/fasttext-vectors/cooking.stackexchange.tar.gz'
f = urllib2.urlopen(url)

with open(filePath, "wb") as code:
    code.write(f.read())

'''Extraxt'''

print("Extracting...")

tar = tarfile.open(filePath)
tar.extractall(path='corpus')
tar.close()

'''Clean'''

print("Cleaning...")

g=open("corpus/cooking-corpus.txt","w")

for line in open("corpus/cooking.stackexchange.txt","r"):
    line2=[]
    line=line.lower()
    line=line.split()
    for word in line:
        if "__label__" in word:
            continue
        line2.append(word)
    g.write(" ".join(line2)+"\n")








