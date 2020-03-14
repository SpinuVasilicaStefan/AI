import numpy as np

def get_data(file):
    f = open(file, "r")
    intrari, iesiri, vectori = list(map(lambda x: int(x),f.readline().split("\t")))
    linie = f.readline()
    listax = []
    listay = []
    while(linie):
        intrare, iesire = linie.split("\t")
        intrare =list(intrare.split(","))
        iesire = list(iesire.split(","))
        intrare = intrare[:len(intrare) - 1]
        iesire = iesire[:len(iesire)]
        iesire = np.array(list(map(lambda x: int(x), iesire)))
        intrare = np.array(list(map(lambda x: int(x), intrare)))
        listax += [intrare]
        listay += [iesire]
        linie = f.readline()
    return np.array(listax), np.array(listay)


def init(hidden):
    weights1 = np.random.rand(hidden, 7) / 5 - 0.1
    weights2 = np.random.rand(10, hidden) / 5 - 0.1
    return [weights1, weights2]

def forward(weights, inputs): #calculez activarea si pentru hidden si pt output
    z1 = weights[0].dot(inputs)
    a1 = sigmoid(z1)
    z1 = weights[1].dot(a1)
    a2 = sigmoid(z1)
    return (a1, a2)

def train(weights, train_x, train_y, learning_rate, epochs, target_error):
    for _ in range(epochs):
        mse = 0
        for i in range(len(train_x)):
            err = backpropagation(weights, train_x[i], train_y[i], learning_rate)
            mse += (err * err).sum()
        mse /= ( len(train_x) * len(train_y[0]) )
        if mse < target_error:
            return

def backpropagation(weights, inputs, outputs, learning_rate):
    (a1, a2) = forward(weights, inputs)
    err = outputs - a2
    delta2 = a2 * (np.ones(a2.shape) - a2) * err
    dW2 = a1.reshape(len(a1), 1).dot(delta2.reshape(1, len(delta2))).T
    weights[1] += learning_rate * dW2

    delta1 = a1 * (np.ones(a1.shape) - a1) * delta2.dot(weights[1])
    dW1 = learning_rate * delta1.reshape(len(delta1), 1).dot(inputs.reshape(1, len(inputs)))
    weights[0] += learning_rate * dW1
    return err


def sigmoid(x):
    print(x)
    return 1 / (1 + np.exp(-x))



def algoritm():
    weights = init(7)
    date = get_data("data.txt")
    train(weights, date[0], date[1], 0.5, 1000, 0.001)
    prediction = forward(weights, date[0][1])[-1].round(2)
    print()
    print(prediction)
algoritm()




#get_data("data.txt")