import numpy as np
import random
import math
from LanguageSys import*




class NeuralNet:
    def __init__(self,x,y,inputs):
        self.x = x
        self.y = y
        self.inputs = inputs

        self.neurons = self.generateMatrix(x,y)
        self.weights = self.generateWeights()
        self.winning = []  #x-y Position of winning neuron
        self.neighbours = [] #matrix of learning affection on the area
        self.distances = [] #only for testing
        self.habitus = [random.uniform(0, 1) for k in range(3)]
        self.width = 10
        self.fitness = 0  #here we can punish or encourage behaviour




    def generateWeights(self):

        myweights = []
        for y in range(self.y):
            tmp = []
            for x in range (self.x):
                tmp.append( self.generateVector(self.inputs))
                    #myweights[y][x].#Generates Vector of weights according to number of inputs
            myweights.append(tmp)
        return myweights

    def generateMatrix(self, x, y):  # Generates random matrix, x =  Number of Neurons /  and y = Number of Inputs

        column = [random.uniform(0, 1) for k in range(x)]

        matrix = [column]  # Create first Column of our weight Matrix
        for i in range(y):
            if i != 0:
                column = [random.uniform(0, 1) for k in range(x)]
                matrix = np.append(matrix, [column], axis=0)

        return matrix

    def generateVector(self, x):  # Generates random vector, x =  number of neurons

        column = [random.uniform(0, 1)]

        matrix = [column]  # Create first Column
        for i in range(x):
            column = [random.uniform(0, 1)]
            if i != 0:
                matrix = np.append(matrix, [column], axis=0)

        return matrix

    ### NOW WE DO THE CALCULATIONS

    def updateNeurons(self, inputs, myrange):  #range = neighbourhood-steps /// range = 0 means no learning except the selected
        self.compareWeights(inputs)   #updates neuron-Values
        self.neighbours = self.neighboursfunc(myrange)
        self.learning(inputs)
        if self.width > 1.1:
            self.width -= 0.1

    def compareWeights(self, input): #splits weight matrix to vectors, compares and returns array of similarity values
        winningVal = 5 # we pick a high number, lowest wins

        for y in range (self.y): #number of neurons
            for x in range (self.x):
                excitement = 0

                for i in range (self.inputs): #calculate value for every input (i =input)
                    excitement += input[i][0] - self.weights[y][x][i][0]

                self.neurons[y][x] = excitement
                if abs(excitement) < winningVal: #now we test for the winning neuron
                    winningVal = abs(excitement)
                    self.winning = [x,y]

    def neighboursfunc(self, myrange): #width of Gaussian TODO: include width to outer functions
        neighbours = []

        for y in range(self.y):

            dist = []
            for x in range(self.x):

                if self.winning[0] != x or self.winning[1] != y:
                    distance = int(math.sqrt((((self.winning[0] - x) ** 2)) + ((self.winning[1] - y) ** 2)))/myrange

                    if distance == 0:
                        distance = 1

                else:
                    distance = 0
                self.distances.append(distance)

                learning = round((1 / math.sqrt(2 * math.pi))* math.e ** -(1/self.width*(distance ** 2)),3)
                dist.append(learning)
            neighbours.append(dist)
        return neighbours

    def learning(self, inputs): #now we bring weights closer to input in dependence of self.neighbours
        for y in range (self.y):
            for x in range (self.x):
                if self.neighbours[y][x] != 0:
                    for i in range (self.inputs):

                        oldweight = self.weights[y][x][i][0]
                        self.weights[y][x][i][0] = oldweight + self.neighbours[y][x] * (inputs[i][0]- oldweight) - self.fitness

    def speak(self):
        myLanguage = LanguageSys()
        return myLanguage.output(self.habitus, self.winning)

    def shapeInput(self, myarray): #shapes input array into vector, needs at least 1 argument
        first = [myarray[0]]
        matrix = [first]
        for i in range (len(myarray)):
            if i != 0:
                next = [myarray[i]]

                matrix = np.append(matrix, [next], axis=0)
        return matrix

    def posval(self, pos): #for testing
        if pos[0] == 0:
            if pos[1] == 0:
                val1 = 0
                val2 = 1

            else:
                val1 = 1
                val2 = 0
        else:
            if pos[1] == 0:
                val1 = 0.1
                val2 = 0.1
            else:
                val1 = 0.01
                val2 = 0.001
        return [val1, val2]
    def punish (self, punishment): #punishes winning weights
        for i in range (self.inputs):

            self.weights[self.winning[0]][self.winning[1]][i][0] -= punishment








if __name__ == '__main__':

    inputs = 3
    myRange = 1

    n = NeuralNet(4,4,inputs)
    #print "Weights before", n.weights


    inputVals = n.generateVector(inputs) #Generating some Input


    # for i in range (10):
    #     n.updateNeurons(inputVals, myRange)
    #     inputVals = n.generateVector(inputs)  # Generating some Input
    #
    #     print "Winning Neuron:", n.winning
    # print "Winning Neuron:",n.winning
    # print "Distances", n.distances # (as array)
    # print "Weights after", n.weights




    data = [[1.00, 0.46, 0.1864695139],[0.96, 0.36 ,0.03775425955],[0.23, 0.49, 1.284095174],[0.19, 0.56, 0.07685956616],[0.15,1.34,0.1998048488],[0.14,0.59,	0.03390127349],[0.12,0.40,	0.03007330681],[0.10,0.53,	0.2196952638],[0.09,0.38,	0.2043333584],[0.09,0.29,	0.8573394381],[0.07,0.57,	0.08091270735],[0.07,0.57,	0.01491155646],[0.07,1.16,	0.07708474067],[0.07,0.22,	0.04656108484],[0.06,0.38,	0.9931697065]]
    countries = ["China","Indien", "Vereinigte Staaten von Amerika","Indonesien" ,"Brasilien" ,"Pakistan",  "Nigeria", "Bangladesch" ,"Russland", "Mexiko","Japan",  "Philippinen","Aethiopien",  "Aegypten",   "Vietnam", "Deutschland" ]



    for j in range (1000):
        print "DURCHGANG NR", j+1
        for i in range (len (data)):
            column = [data[i][0]]
            column1 = [data[i][1]]
            column2 = [data[i][2]]
            matrix = [column]
            matrix = np.append(matrix, [column1], axis = 0)
            matrix = np.append(matrix, [column2], axis = 0)
            inputVals = matrix
            n.updateNeurons(inputVals, myRange)

            print countries[i], "WINNING NEURON", n.winning
        print ""


