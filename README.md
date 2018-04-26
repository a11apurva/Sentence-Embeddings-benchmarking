# Sentence Embeddings Benchmarking

Comparison of [word2vec](https://radimrehurek.com/gensim/models/word2vec.html) and [fasttext](https://github.com/facebookresearch/fastText) for sentence-embedding using:

1. [SIF (Smooth Inverse Frequency)](https://github.com/PrincetonML/SIF)
2. Simple summation of word-vectors

## Dataset

cooking.stackexchange(49.2MB) from https://archive.org/download/stackexchange/

Use `make_corpus.py` to Download, Extract and Clean the cooking-corpus

## Word Embeddings

Pre-trained word embedings produced by word2vec and fasttext is provided in the `Data` folder. 
Same hyper-parameters were used in both the algorithms.

One can go through [word2vec](https://radimrehurek.com/gensim/models/word2vec.html) and [fasttext](https://github.com/facebookresearch/fastText) to generate their own vectors with different hyper-parameters.

## Sentence Embeddings

Although many algorithms exist for word-embedding but very few are present for generating sentence vectors. 
Here we will see two basic approaches for achieving it.

1. **SIF** : Represent the sentence by a weighted average of the word vectors, and then modify them using Principal Component Analysis. ([Paper](https://openreview.net/forum?id=SyK00v5xx))
2. **Summation** : Represent the sentence by simply adding the word vectors.

## Results

Test Set :
```
0. how to cook vanilla biscuits 
1. my computer is not working
2. I want to bake a cake
3. I really dont like physics
4. can I get a delicious apple pie
5. fire is dangerous in kitchen
6. I need a new laptop
```
Note : The words *computer*, *laptop* and *physics* are not in the training corpus.
 
 **Using SIF :**
 ```
[line1 , line2 , cosine-score]

word2vec:
[1, 3, 0.3615238794780853]
[1, 5, 0.16758663036793786]
[3, 5, 0.06426503942327821]
[2, 5, 0.055325088436649184]
[1, 4, 0.044131843175960306]

fasttext
[1, 5, 0.4629584213919866]
[1, 3, 0.3335793994296907]
[3, 6, 0.2851278825589737]
[5, 6, 0.28461824462454666]
[3, 5, 0.22888942154014358]
```


//Results to be added for Summation

## TODO: 
1. Experiment with Glove
2. Weighted average without PCA removal
3. Detailed Readme and Documentation

