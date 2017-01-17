# RNN_Text_Classify

- [tensorflow实现基于LSTM的文本分类方法](http://blog.csdn.net/u010223750/article/details/53334313)
- [LSTM Networks for Sentiment Analysis](http://deeplearning.net/tutorial/lstm.html)
This code belongs to the "implement a RNN for text classification in Tensorflow" POST<br/>
Contrast with [IMPLEMENTING A CNN FOR TEXT CLASSIFICATION IN TENSORFLOW](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)



#How to run

bob@bob-OptiPlex-3020:~/workspace/github/RNN_Text_Classify$ python3 train_rnn_classify.py <br/>
loading the dataset...<br/>
load data from %s data/subj0.pkl<br/>
begin training<br/>
WARNING:tensorflow:From train_rnn_classify.py:145 in train_step.: all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2016-03-02.<br/>
Instructions for updating:<br/>
Please use tf.global_variables instead.<br/>
WARNING:tensorflow:From train_rnn_classify.py:148 in train_step.: initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.<br/>
Instructions for updating:<br/>
Use `tf.global_variables_initializer` instead.<br/>
the 1 epoch training...<br/>
the 100 step, train cost is: 0.684807 and the train accuracy is 0.593750 and the valid accuracy is 0.495556<br/>
Saved model chechpoint to/home/bob/workspace/github/RNN_Text_Classify/runs/checkpoints/model-127<br/>
<code>tensorboard --logdir ./runs/summaries/</code?


#Requirements
Python 2.7/3.5
Tensorflow > 1.1/0.12.0rc0
Numpy





#Training
train_rnn_classify.py

#note
*this code save the model checkpoints and save the summary at given epoch, these actions will slow down the training speed,so if you want to do a quick job, just remove these codes if you need<br/>
*dataset_path='data/subj0.pkl' 请问文件格式和内容<br/>
是文本词表的单词索引，比如“I love the movie”对应的就是[1,2,3]等（举个例子），索引是按照词频的排序从高往低排列的
train_set_y里面是类别的索引，比如4分类索引就是0，1，2，3这四个数，因为我损失函数里面用到的是sparse_softmax_loss，当然你这种one-hot的写法也是可以的，对应的损失函数就是softmax_loss，对结果没有影响（当然代码调整下维度就行）<br/>
*代码中data的target，也就是y是怎么设的呢，是最终的分类目标吗？ 我能拿到mean_pooling的输出h吗<br/>
target就是分类的目标，也就是类别标签，可以拿到mean-pooling的h，在代码中加上fetches加上h就行了<br/>
*mask的作用是什么<br/>
tensorflow输入矩阵是指定的，但是一个batch的句子长度可能是不定的，所以需要进行padding，但是padding的数据是最后不能参与分类的，所以需要mask标记一下<br/>

