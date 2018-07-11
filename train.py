import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse

#p = get_traindata()



#scores = np.dot(p,w)
    
def getLoss(w,x,lam,i):
    m = x.shape[0] #First we get the number of training examples
    y_mat = oneHotIt() #Next we convert the integer class coding into a one-hot representation
    scores = np.dot(x,w) #Then we compute raw class scores given our input and current weights
    prob = softmax(scores) #Next we perform a softmax on these scores to get their probabilities
    loss = (-1 / m) * np.sum(np.log(prob) * y_mat) + (lam/2)*np.sum(w) #We then find the loss of the probabilities
    grad = (-1 / m) * np.dot(x.T,(prob)) + lam*w #And compute the gradient for that loss
    return loss,grad

def oneHotIt():
    #Y = Y[:,0]
    col = np.array([0,1,2])
    brr = [0,1,2]
    y = scipy.sparse.csr_matrix((np.ones(3),(brr,col)))
    y = y.todense().T
    return y

def softmax(z):
    z -= np.max(z)
    sm = (np.exp(z).T / np.sum(np.exp(z),axis=1).T).T
    return sm

def getProbsAndPreds(someX):
    w = np.load("weight.pickle")
    loss,grad = getLoss(w,someX,1,0)
    probs = grad[:,0]
    preds = [float(probs[0]),float(probs[1]),float(probs[2]),float(probs[3]),float(probs[4]),float(probs[5])]
    return preds

def train(p):
    w = np.load("weight.pickle")
    lam = 1
    iterations = 1000
    learningRate = 1e-15
    losses = []
    for i in range(0,iterations):
        loss,grad = getLoss(w,p,lam,i)
        losses.append(loss)
        w = w - (learningRate * grad)
    w.dump("weight.pickle")
    return plt.plot(losses)