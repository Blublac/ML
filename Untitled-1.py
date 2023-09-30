 # Launch the graph in a session.

import tensorflow as tf

with tf.compat.v1.Session() as ses:

     # Build a graph.
     a = tf.constant(5.0)
     b = tf.constant(6.0)
     c = a * b
     msg = tf.constant('hello')
     print (ses.run(msg))
     # Evaluate the tensor `c`.
     print(ses.run(c))


    