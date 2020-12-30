import numpy as np

def GauseP(data_y:list):

    def kernel(x, x_prime, p, q, r) :
        if x == x_prime:
            delta = 1
        else:
            delta = 0
        return p*np.exp(-1 * (x - x_prime)**2 / q) + ( r * delta)


    data_y = np.array(data_y)
    n = len(data_y)
    data_x = np.arange(0.01,(n+1)/100,0.01)

    missing_value_rate = 0.2
    sample_index = np.sort(np.random.choice(np.arange(n), int(n*missing_value_rate), replace=False))

    #learning data
    xtrain = np.copy(data_x[sample_index])
    ytrain = np.copy(data_y[sample_index])
    xtest = np.copy(data_x)

    #average
    mu = []
    #var
    var = []

    #params
    Theta_1 = 1.0
    Theta_2 = 0.2
    Theta_3 = 0.2
    
    #Gause
    train_length = len(xtrain)
    K = np.zeros((train_length, train_length))

    for x in range(train_length):
        for x_prime in range(train_length):
            K[x, x_prime] = kernel(xtrain[x], xtrain[x_prime], Theta_1, Theta_2, Theta_3)
    
    yy = np.dot(np.linalg.inv(K), ytrain)
    test_length = len(xtest)
    for x_test in range(test_length):
        k = np.zeros((train_length,))
        for x in range(train_length):
            k[x] = kernel(xtrain[x], xtest[x_test], Theta_1, Theta_2, Theta_3)

        s = kernel(xtest[x_test], xtest[x_test], Theta_1, Theta_2, Theta_3)
        mu.append(np.dot(k, yy))
        kK_ = np.dot(k, np.linalg.inv(K))
        var.append(s - np.dot(kK_, k.T))
    
    return data_x, data_y, xtest, sample_index, var, mu