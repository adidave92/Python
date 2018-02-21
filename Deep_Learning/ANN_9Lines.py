from numpy import random,exp,dot,array

i=array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
o=array([[0,1,1,0]]).T

random.seed(1)
w=2*random.random((3,1))-1

for x in range(1000):
    out=1/(1+exp(-(dot(i,w))))
    w += dot(i.T,(o-out)*out*(1-out))
print(1/(1+exp(-(dot([1,0,0],w)))))
