import tensorflow as tf
import numpy as np

# create data
x_data=np.random.rand(100).astype(np.float)
y_data=x_data*0.1+0.3

# create model
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros(1))

y=Weights*x_data+biases

# calculate the errors
loss=tf.reduce_mean(tf.square(y-y_data))

# errors feedback
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

# Training:
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 ==0:
        print(step,sess.run(Weights),sess.run(biases))