import numpy as np

class Perceptron:
    def __init__(self, nbInput, nbEpochs, learningRate, nbWeight):
        self.nbInput = nbInput
        self.nbEpochs = nbEpochs
        self.learningRate = learningRate
        self.weight = np.zeros(nbWeight)
        self.biais = [1., 0.]

    def predict(self, input1, input2):
        y = self.biais[0]*self.biais[1] + input1*self.weight[0] + input2*self.weight[1]
        if(y <= 0):
            y = 0
        else:
            y = 1
        return y