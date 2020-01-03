# import load_data
import keras
import matplotlib.pyplot as plt
import datetime
import os
import numpy as np
import tensorflow as tf
#import keypoller

def generate_data(samples):
  # x = np.random.normal(loc=0.0, scale=1.0, size=(samples, 2))

  x = np.concatenate((
    np.random.normal(loc=0.0, scale=0.5, size=(samples // 2)),
    np.random.normal(loc=0.0, scale=1.0, size=(samples // 2)),
    np.random.normal(loc=0.0, scale=10.0, size=(samples // 2)),
    np.random.normal(loc=0.0, scale=100.0, size=(samples // 2))
  ))
  x = np.abs(x)
  np.random.shuffle(x)
  x = np.reshape(x, (samples, 2))

  y = np.multiply(x[:, 0], x[:, 1])
  y = np.reshape(y, [samples, 1])
  print (x[0:10,:])
  print (y[0:10])

  train_val_split = 0.9
  train_size = int(len(x) * train_val_split)
  x_train = np.array(x[:train_size])
  y_train = np.array(y[:train_size])
  x_val = np.array(x[train_size:])
  y_val = np.array(y[train_size:])

  print('')
  print('x_train: ', x_train.shape)
  print('y_train: ', y_train.shape)
  print('x_val: ', x_val.shape)
  print('y_val: ', y_val.shape)
  print('')
  return x_train, y_train, x_val, y_val

@tf.custom_gradient
def nlrelu(x):
  x2 = tf.maximum(x, 0.0) + 1.0
  def grad(dy):
    return tf.divide(dy, x2)
  return tf.log(x2), grad

@tf.custom_gradient
def exp(x):
  result = tf.exp(x)
  def grad(dy):
    return dy * result
  return result, grad

@tf.custom_gradient
def huber(x):
  def grad(dy):
    return tf.where(tf.less(tf.abs(x), 0.5), dy*2.0*x, dy * tf.sign(x))
  result = tf.where(tf.less(tf.abs(x), 0.5), x*x, tf.abs(x))
  return result, grad

n_samples=100000
x_train, y_train, x_val, y_val = generate_data(n_samples)

x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])

L1_INPUT = 2
L1_OUTPUT = 20
wd1 = tf.Variable(tf.truncated_normal([L1_INPUT, L1_OUTPUT], mean=0.0, stddev=0.03), name='wd1')
bd1 = tf.Variable(tf.truncated_normal([L1_OUTPUT], mean=0.0, stddev=0.03), name='bd1')
dense_layer1 = tf.matmul(x, wd1) + bd1
dense_layer1 = tf.concat([nlrelu(dense_layer1[:, 0:10]), tf.nn.relu(dense_layer1[:,10:])], 1)
# dense_layer1 = tf.nn.relu(dense_layer1)

L2_INPUT = L1_OUTPUT
L2_OUTPUT = 20
wd2 = tf.Variable(tf.truncated_normal([L2_INPUT, L2_OUTPUT], mean=0.0, stddev=0.03), name='wd2')
bd2 = tf.Variable(tf.truncated_normal([L2_OUTPUT], mean=0.0, stddev=0.03), name='bd2')
dense_layer2 = tf.matmul(dense_layer1, wd2) + bd2
dense_layer2 = tf.concat([exp(dense_layer2[:, 0:10]), tf.nn.relu(dense_layer2[:,10:])], 1)
# dense_layer2 = tf.nn.relu(dense_layer2)


L3_INPUT = L2_OUTPUT 
L3_OUTPUT = 1
wd3 = tf.Variable(tf.truncated_normal([L3_INPUT, L3_OUTPUT], mean=0.0, stddev=0.03), name='wd3')
bd3 = tf.Variable(tf.truncated_normal([L3_OUTPUT], mean=0.0, stddev=0.03), name='bd3')
dense_layer3 = tf.matmul(dense_layer2, wd3) + bd3


prediction = dense_layer3
loss_weights = tf.divide(tf.ones_like(y), tf.maximum(0.01, tf.abs(y))) # tf.where(tf.less(tf.abs(y), 0.0001), tf.abs(y), tf.multiply(y, y)))
# loss = tf.reduce_mean(tf.multiply(tf.abs(tf.subtract(prediction, y)), loss_weights))
# loss = tf.reduce_mean(tf.multiply(tf.squared_difference(prediction, y), loss_weights))
# loss = tf.reduce_mean(tf.squared_difference(prediction, y))
loss = tf.reduce_mean(tf.multiply(huber(tf.subtract(prediction, y)), loss_weights))

# L1_REG_BETA = 0.0001
# l1_norm = tf.reduce_sum([
#   tf.reduce_sum(tf.abs(wd1)),
#   tf.reduce_sum(tf.abs(wd2)),
#   tf.reduce_sum(tf.abs(wd3)),
#   # tf.reduce_sum(tf.abs(wd4)),
#   # tf.reduce_sum(tf.abs(wd5)),
# ])
# l1_reg = tf.multiply(L1_REG_BETA, l1_norm, name="l1_reg")
L2_REG_BETA = 0.0000 # 0.00005
l2_norm = (
  tf.nn.l2_loss(wd1) + 
  tf.nn.l2_loss(wd2) + 
  tf.nn.l2_loss(wd3)
)
l2_reg = tf.multiply(L2_REG_BETA, l2_norm, name="l2_reg")
reg_loss = tf.add(loss, l2_reg, name="reg_loss")
loss_summary = tf.summary.scalar(name="loss", tensor=reg_loss)
val_loss_summary = tf.summary.scalar(name="val_loss", tensor=reg_loss)

learning_rate=0.0001
learning_rate_placeholder = tf.placeholder(tf.float32, [], name='learning_rate')
optimiser = tf.train.AdamOptimizer(
  learning_rate=learning_rate_placeholder,
  beta1=0.9,
  beta2=0.999,
  epsilon=1e-8).minimize(reg_loss)


batch_size = 2000

init_op = tf.global_variables_initializer()

def get_batch(i):
  start_index = i*batch_size
  end_index = i*batch_size + batch_size
  if end_index > len(x_train):
    return x_train[start_index:], y_train[start_index:]
  return x_train[start_index:end_index], y_train[start_index:end_index]

logs_dir = os.path.join('./logs_multiply', datetime.datetime.now().strftime('tf-%Y%m%d-%H%M'))
epoch = 0
last_loss = 0
loss_delta = 0

with tf.Session() as sess:
  file_writer = tf.summary.FileWriter(logs_dir, sess.graph)
  sess.run(init_op)
  total_batches = (len(x_train) + batch_size - 1) // batch_size
  
  
  def run_training_epoch():
    global epoch
    global last_loss
    global loss_delta

    avg_loss = 0
    avg_reg_loss = 0
    for i in range(total_batches):
        batch_x, batch_y = get_batch(i)
        _, computed_loss, computed_reg_loss, summary, pred = sess.run(
            [optimiser, loss, reg_loss, loss_summary, prediction], 
            feed_dict={x: batch_x, y: batch_y, learning_rate_placeholder: learning_rate})
        avg_loss += computed_loss / total_batches
        avg_reg_loss += computed_reg_loss / total_batches
        file_writer.add_summary(summary, epoch)

    if epoch % 100 == 0:
      val_loss, val_summary = sess.run([loss, val_loss_summary], feed_dict={x: x_val, y: y_val})
      file_writer.add_summary(val_summary, epoch)

      if last_loss:
        loss_delta = 100 * (avg_loss - last_loss) / last_loss
      last_loss = avg_loss

      print("Epoch:", (epoch + 1),
            ", avg_reg_loss: {:.4f}".format(avg_reg_loss), 
            ", loss: {:.4f}".format(avg_loss), 
            ", val_loss: {:.4f}".format(val_loss),
            ", loss delta: {:.2f}%".format(loss_delta))
    epoch += 1
    
  def print_weights():
    wd1_value, bd1_value, wd2_value, bd2_value, wd3_value, bd3_value = sess.run(
      [wd1, bd1, wd2, bd2, wd3, bd3])
    print("\n wd1_value:\n", wd1_value)
    print("\n bd1_value:\n", bd1_value)
    print("\n wd2_value:\n", wd2_value)
    print("\n bd2_value:\n", bd2_value)
    print("\n wd3_value:\n", wd3_value)
    print("\n bd3_value:\n", bd3_value)

  def run_test():
    x_test = [
      [0.5, 0.5],
      [0.5, 1.0], 
      [1.0, 0.5], 
      [0.3, 0.3],
      [0.7, 0.7],
      [0.7, 0.5],
      [0.5, 0.7],
      [1.0, 1.0],
      [1.5, 0.8],
      [0.8, 1.5],
      [2.0, 2.0],
      [5.0, 2.5],
      [3.25, 4.0],
      [10.0, 10.0],
      [25.0, 25.0],
      [100.0, 100.0],
      [1000.0, 1000.0],
      [2, 1000.0],
      [0.01, 100.0],
      [0.001, 1000.0],
      [10000.0, 10000.0],
      [0.0001, 10000.0],
      [0.01, 0.01],
      [0.001, 0.001],
      [0.0001, 0.0001],
      [10000.0, 0],
      [1.0, 0],
      [0.0001, 0],
    ]
    pred = sess.run([prediction], feed_dict={x: x_test})
    # print(pred)
    for i in range(len(x_test)):
      print(x_test[i][0], "*", x_test[i][1], "=", pred[0][i][0])

  def adjust_learning_rate(factor):
    global learning_rate
    learning_rate = learning_rate * factor
    print ("new learning_rate: ", learning_rate)

  n_epochs=400
  for c_epoch in range(n_epochs):
    run_training_epoch()
    #print(f'finished epoch {c_epoch+1}')
  run_test()
  print_weights()

  #keyboard_poller = keypoller.KeyPoller()
  #while True:
  #  run_training_epoch()
  #  pressed = keyboard_poller.poll()
  #  if pressed == 't':
  #    run_test()
  #  if pressed == 's':
  #    run_test()
  #    break
  #  if pressed == 'p':
  #    print_weights()
  #  if pressed == '.':
  #    adjust_learning_rate(2.0)
  #  if pressed == ',':
  #    adjust_learning_rate(0.5)
  
print("\nTraining complete!")
