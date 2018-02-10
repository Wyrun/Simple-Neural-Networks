# (c) 2018 Max Shytov | Wyrun

import random

e = 2.71828182845904


def sigmoid(x):
    res = 1
    res /= (1 + pow(e, -x))
    return res

class neuron:
    def __init__(self, weightAmount, ifGetSt):
        self.ifGetSt = ifGetSt
        self.weightAmount = weightAmount
        self.weights = []
        self.currentValue = float(0)
        self.previousValue = float(0)
        for i in range(self.weightAmount):
            self.weights.append(float(0))
    def newValue(self, theValue):
        self.previousValue = self.currentValue
        self.currentValue = theValue
        if self.ifGetSt:
            self.currentValue = sigmoid(self.currentValue)

    def randMyWeights(self):
        self.weights = list(map(lambda : random.randint(0,1000)/500 - 1, self.weights))

class NN:
    def __init__(self, inputAmount, outputAmount, hiddenLayersAmount, neuronsOnEachLayer, ifInputsGetSt):
        self.inputAmount = inputAmount
        self.outputAmount = outputAmount
        self.hiddenLayersAmount = hiddenLayersAmount
        self.neuronsOnEachLayer = neuronsOnEachLayer
        self.inputs = []
        self.outputs = []
        self.hidden = []
        for i in range(self.inputAmount):
            self.inputs.append(neuron(self.neuronsOnEachLayer, ifInputsGetSt))
        for i in range(self.outputAmount):
            self.outputs.append(neuron(0, True))
        for i in range(self.hiddenLayersAmount - 1):
            self.hidden.append([])
            for j in range(self.neuronsOnEachLayer):
                self.hidden[i].append(neuron(self.neuronsOnEachLayer, True))
        self.hidden.append([])
        for j in range(self.neuronsOnEachLayer):
            self.hidden[i].append(neuron(self.outputAmount, True))

    def run(self, inputs):
        for i in range(self.inputAmount):
            self.inputs[i].newValue(float(inputs[i]))
        for i in range(self.neuronsOnEachLayer):
            newValue = float(0)
            for j in range(self.inputAmount):
                newValue += self.inputs[j].currentValue * self.inputs[j].weights[i]
            self.hidden[0][i].newValue(newValue)
        for h in range(self.hiddenLayersAmount - 1):
            for i in range(self.neuronsOnEachLayer):
                newValue = float(0)
                for j in range(self.neuronsOnEachLayer):
                    newValue += self.hidden[h][j].currentValue * self.hidden[h][j].weights[i]
                self.hidden[h + 1][i].newValue(newValue)

        for i in range(self.outputAmount):
            newValue = float(0)
            for j in range(self.neuronsOnEachLayer):
                newValue += self.hidden[self.hiddenLayersAmount - 1][j].currentValue * self.hidden[self.hiddenLayersAmount - 1][j].weights[i]
            self.outputs[i].newValue(newValue)
        res = []
        for i in range(len(self.outputs)):
            res.append(self.outputs[i].currentValue)
        return res

    def randomizeTheWeights(self):
        for i in range(self.inputAmount):
            self.inputs[i].randMyWeights
        for i in range(self.hiddenLayersAmount):
            for j in range(len(self.hidden[i])):
                self.inputs[i].randMyWeights
        return True
    def Learn(self, DataX, DataY):

MyNN = NN(1,1,1,1, False)
MyNN.randomizeTheWeights()

print(MyNN.run([1]));
