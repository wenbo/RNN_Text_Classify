import word2vec
model = word2vec.load('corpusWord2Vec.bin')
print (model.vectors)
index = 1
print (model.vocab[1])
print (model.vocab)
