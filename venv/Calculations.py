import random
import numpy as np
import math



class Calculations():


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

    def generateVectorlist(self, ins, neurons):
        allweights = []
        for i in range (neurons):
            allweights.append(self.generateVector(ins))
        return allweights

    def compareVectors(self, ins, vector):
        compareVal = 0
        for i in range(len (ins)):
            compareVal += ins[i][0] - vector[i][0]
        return compareVal

    def compareWeights(self, ins, allweights): #splits weight matrix to vectors, compares and returns array of similarity values
        similarity = []
        for i in range (len(allweights)):

            similarity.append(self.compareVectors(ins, allweights[i]))

        return similarity #returns a list with length of neurons with general similartiy to overall input

    def winningNeuron(self, ins, similarity): #finds pos of winning neuron
        value = 1 #"winning" value
        for i in range (len(similarity)):
            if abs(similarity[i]) < value:
                value = abs(similarity[i])
                winning = i
        return winning

    def neighbours(self, x, y, winning): #x = rows; y = columns

        winning += 1 #we need this for our method
        space = True


        #now we measure how many steps we can go from winning neuron diagonally (default: We can go at least 1 step in every direction)
        left = 0
        right = 0
        upleft = 0
        up = 0
        upright = 0
        downleft = 0
        down = 0
        downright = 0


        buffer = winning #the point from where we are looking at

        #upleft
        while space == True:
            if buffer % x == 1: #if buffer is firt item in row we only go up
                if (buffer - x) >= 0:
                    up += 1 #gets checked only once
                    buffer = buffer - x
                else:
                    space = False
            elif (buffer - x) - 1 >= 0:
                upleft += 1
                buffer = (buffer - x) - 1 #now buffer is set to next point

            else:
                space = False #if there is no more neuron


        # Resetting Values
        space = True
        buffer = winning


        # upright
        while space == True:
            if upleft + up == 0: #if we can't go up at all this isn't executed
                space = False
            elif buffer % x == 0: #Checks if buffer is set on last item in a column
                space = False #If we can only go up
            elif (buffer - x) + 1 > 0:
                upright += 1
                buffer = (buffer - x) + 1  # now buffer is set to next point
            else:
                space = False  # if there is no more neuron



        # Resetting Values
        space = True
        buffer = winning




        # downleft
        while space == True:
            if buffer % x == 1: #if buffer is firt item in row we only go down
                if (buffer + x) <= x * y :
                    down += 1 #gets checked only once
                    buffer = buffer + x
                else:
                    space = False
            elif (buffer + x ) - 1 <= x * y :
                downleft += 1
                buffer = (buffer + x) - 1 #now buffer is set to next point
            else:
                space = False #if there is no more neuron

        # Resetting Values
        space = True
        buffer = winning





        # downright
        while space == True:
            if downright + down == 0: #if we can't go up at all this isn't executed
                space = False
            elif buffer % x == 0: #Checks if buffer is set on last item in a column
                space = False #If we can only go down
            elif (buffer + x) + 1 <= x*y:
                downright += 1
                buffer = (buffer + x) + 1  # now buffer is set to next point
            else:
                space = False  # if there is no more neuron


        distancelist = []


        if upleft + up > downleft + down:
            maxdistance = upleft + up
        else:
            maxdistance = downleft + down

        for i in range (maxdistance):
            distancelist.append([])
        print distancelist

        # now we find out the edges of the edges of different distances

        right = (winning % x) - x
        left  = (winning % x) - 1


















#
# if __name__ == '__main__':
#
#     --> neue inputs
#     --> summe allen inputs( input - gewicht)
#     --> neuronrn speichen attraction
#     --> winner = mit der niedrigsten Attraction
#     --> winner weights = annährung an input
#     --> in der distanz liegenden Neuronen lernen mit



