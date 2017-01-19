import word2vec
word2vec.word2vec('/home/bob/workspace/github/RNN_Text_Classify/word2vec/corpusSegDone.txt', '/home/bob/workspace/github/RNN_Text_Classify/word2vec/corpusWord2Vec.bin', size=300,verbose=True)
word2vec.doc2vec('/home/bob/workspace/github/RNN_Text_Classify/word2vec/corpusSegDone.txt', '/home/bob/workspace/github/RNN_Text_Classify/word2vec/corpusWord2Vec.bin', size=300,verbose=True)
