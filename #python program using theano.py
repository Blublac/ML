#python program using theano
#computing a logistic
#function

import theano 
import theano.tensor as T
x= T.dmatrix('x')
s= 1/(1+T.exp(-x))
logistic= theano.function([x], s)
logistic([[0,1],[-1,-2]])

