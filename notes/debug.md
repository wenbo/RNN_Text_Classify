# http://blog.csdn.net/yhl_leo/article/details/50619029, namely https://www.tensorflow.org/get_started/basic_usage
global_steps=run_epoch(model,session,train_data,global_steps,valid_model,valid_data,train_summary_writer,dev_summary_writer)
def assign_new_batch_size(self,session,batch_size_value):
  session.run(self._batch_size_update,feed_dict={self.new_batch_size:batch_size_value})

valid_accuracy=evaluate(valid_model,session,valid_data,global_steps,valid_summary_writer)

import numpy as np
train_set_x = ["I", "am", "pleased", "to", "meet", "you"]
n_samples= len(train_set_x)
n_train=3
sidx = np.random.permutation(n_samples)

train_set_x = [train_set_x[s] for s in sidx[:n_train]]
print(train_set_x)

  (Pdb) train_set_x[0]
  [1200, 10, 140, 1433, 8, 359, 4, 677, 17969, 235]
  (Pdb) train_set_x[-1]
  [358, 21, 4, 3462, 9397, 10072, 19340, 2222, 535, 17, 5062, 18479, 11, 1286, 186, 1266, 594, 3, 1901, 2179, 10, 4, 52, 7, 1083, 12287, 2745, 94, 7516, 3, 5, 19763, 7, 118, 49, 1679, 26, 123, 32, 5, 2771, 7, 536, 71, 4, 18365, 3, 18, 1511, 800, 25, 7516, 8, 501, 5, 1986, 2081, 8, 34, 5388, 71, 1, 3, 4, 226, 7, 5, 7500, 2935, 26, 10, 1860, 1190, 9, 57, 15, 4, 12237, 71, 9220, 3, 5, 1486, 970, 26, 28, 10576, 6, 5285, 161, 8, 5, 426, 815, 71, 9585, 17476, 3, 5, 7875, 1511, 15, 18, 6212, 7132, 71, 6, 1, 3, 9220, 11, 1, 1114, 505, 15, 5, 935, 4513, 9, 14, 2716, 2]
  (Pdb) len(train_set_x[-1])
  122
  (Pdb) len(train_set_x)
  8100
