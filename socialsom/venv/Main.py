from NeuralNet import*
inputs = 2
myRange = 1

myNet1 = NeuralNet(3,3, inputs)
myNet2 = NeuralNet(3,3, inputs)


myinput = myNet1.shapeInput([0, 0,0,0,0,0, 0,0,0,0])

myNet1.updateNeurons(myinput, myRange)
myinput = myNet1.shapeInput([0, 0,0,0,0,0, 0,0,0,0])

myNet2.updateNeurons(myinput, myRange)

myinput = myNet1.shapeInput(myNet2.speak())

###conversation


change = 0

for i in range (10000):
    myinput = myNet1.shapeInput(myNet2.winning)
    myNet1.updateNeurons(myinput, myRange)
    print "Person 1: " , myNet1.winning


    myinput = myNet1.shapeInput(myNet2.winning)
    myNet2.updateNeurons(myinput, myRange)
    print "Person 2: ",myNet2.winning

    distance = float(math.sqrt((((myNet1.winning[0] - myNet1.winning[1]) ** 2)) + ((myNet2.winning[0] - myNet2.winning[1]) ** 2))/10)
    if distance >= change:
        change = distance
        if distance > 0:
            myNet1.fitness += 0.1
            myNet2.fitness += 0.1
    else:
        myNet1.fitness = 0
        myNet2.fitness =0
print myNet1.neurons
print myNet1.weights