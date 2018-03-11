class LanguageSys:

    def output(self,myhabitus, neuron): #winning neuron and habitus
        #now we make 10 outputs from habitus and neuron
        myoutput = []
        for i in range (9):
            if i <= 3:

                value = myhabitus[0] * neuron[0]
                myoutput.append(value)
            if i <= 6:
                value = myhabitus[1] * neuron[1]
                myoutput.append(value)
            if i <= 9:
                value = myhabitus[2] * neuron[1]
                myoutput.append(value)
        return myoutput
