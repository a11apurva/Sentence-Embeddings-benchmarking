import sys
sys.path.append('src')
import data_io, params, SIF_embedding

# input
wordfile = '../data/fasttext_model_cooking.txt' # word vector file, can be downloaded from GloVe website
weightfile = 'auxiliary_data/enwiki_vocab_min200.txt' # each line is a word and its frequency
weightpara = 1e-3 # the parameter in the SIF weighting scheme, usually in the range [3e-5, 3e-3]
rmpc = 1 # number of principal components to remove in SIF weighting scheme
sentences = ['this is an example sentence', 'this is another sentence that is slightly longer']


#sentences = ['this is an example sentence', 'this is another sentence that is slightly longer']

sentences =['how to cook vanilla biscuits ',
'my computer is not working',
'i want to bake a cake',
'I really dont like physics',
'can I get a delicious apple pie',
'fire is dangerous in kitchen',
'I need a new laptop']



# load word vectors
(words, We) = data_io.getWordmap(wordfile)
# load word weights
word2weight = data_io.getWordWeight(weightfile, weightpara) # word2weight['str'] is the weight for the word 'str'
weight4ind = data_io.getWeight(words, word2weight) # weight4ind[i] is the weight for the i-th word
# load sentences
x, m = data_io.sentences2idx(sentences, words) # x is the array of word indices, m is the binary mask indicating whether there is a word in that location
w = data_io.seq2weight(x, m, weight4ind) # get word weights

# set parameters
params = params.params()
params.rmpc = rmpc
# get SIF embedding
embedding = SIF_embedding.SIF_embedding(We, x, w, params) # embedding[i,:] is the embedding for sentence i

f=open('data/fasttext_sentence_embeddings.txt','w')
for i in range(len(embedding)):
    rounded = [ round(elem, 6) for elem in embedding[i,:] ]
    #print rounded
    rounded = map(str,rounded)
    rounded = " ".join(rounded)
    f.write(rounded+"\n")
f.close()
    
    
