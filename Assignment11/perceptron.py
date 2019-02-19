#Input - inputs and weights
#Return - 0 or 1 using activation definition
#Use equation (2)
def activation(inputs,weights):
    if weights[0]*inputs[0] + weights[1]*inputs[1] + weights[2]*inputs[2] > 0:
        return 1
    else:
        return 0

#learning rate
nu = .25

#Input - weights and function
#Return updated weights using update function
#Use equation (5)
def update(weights,fp):
    result = activation(fp[0],weights)
    for i in range(0,len(fp[0])):
        weights[i] = weights[i] + nu*(fp[1] - result)*fp[0][i]


#Input - weights and function
#Return - updated a number that reflects error
# 0 means no error
def test(weights,f):
    sum = 0
    for fp in f:
        input = fp[0]
        output = fp[1]
        sum += (output - activation(input,weights))**2
    print("Error: {0}".format(sum**.5))

#Function to be learned including bias
f = [[[-1,0,0], 0], [[-1,0,1],1], [[-1,1,0],1], [[-1,1,1],1]]
#Randomly assigned small weights
weights = [-.05,-0.02,.02]


for i in range(0,10):
    print(weights)
    update(weights,f[i%4])
    test(weights,f)
