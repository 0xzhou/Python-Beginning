from __future__ import print_function
import tensorflow as tf
import os

# define some constant values
a=tf.constant(5.0,name="a")
b=tf.constant(10.0,name="b")

# some basic operations
x=tf.add(a,b,name="add")
y=tf.div(a,b,name="divide")

# run the session
with tf.Session() as sess:
    print("a =", sess.run(a))
    print("b =", sess.run(b))
    print("a + b =", sess.run(x))
    print("a/b =" , sess.run(y))

sess.close()