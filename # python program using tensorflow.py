# python program using tensorflow
#for multiplying two arrarys


#import tensorflow
import tensorflow as tf

#initialize two costants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])




#initialize the session 
sess = tf.compat.v1.Session()

#multiply

result = tf.multiply(x1,x2)



#print the result
print(sess.run(result))


#close session
sess.close()