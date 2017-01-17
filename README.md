# RNN_Text_Classify

This code belongs to the "implement a RNN for text classification in Tensorflow" POST

- [tensorflow实现基于LSTM的文本分类方法](http://blog.csdn.net/u010223750/article/details/53334313)
- [LSTM Networks for Sentiment Analysis](http://deeplearning.net/tutorial/lstm.html)


#How to run

bob@bob-OptiPlex-3020:~/workspace/github/RNN_Text_Classify$ python3 train_rnn_classify.py 
loading the dataset...
load data from %s data/subj0.pkl
begin training
WARNING:tensorflow:From train_rnn_classify.py:145 in train_step.: all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2016-03-02.
Instructions for updating:
Please use tf.global_variables instead.
WARNING:tensorflow:From train_rnn_classify.py:148 in train_step.: initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.
Instructions for updating:
Use `tf.global_variables_initializer` instead.
the 1 epoch training...
the 100 step, train cost is: 0.684807 and the train accuracy is 0.593750 and the valid accuracy is 0.495556
Saved model chechpoint to/home/bob/workspace/github/RNN_Text_Classify/runs/checkpoints/model-127
<code>tensorboard --logdir ./runs/summaries/</code?


#Requirements
Python 2.7/3.5
Tensorflow > 1.1/0.12.0rc0
Numpy





#Training
train_rnn_classify.py

#note
this code save the model checkpoints and save the summary at given epoch, these actions will slow down the training speed,so if you want to do a quick job, just remove these codes if you need
