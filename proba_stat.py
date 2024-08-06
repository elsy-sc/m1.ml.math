# random variable

## Considérons un dé à 6 faces, la variable aléatoire X est le résultat du dé
## X = {1, 2, 3, 4, 5, 6}
## X est une variable aléatoire discrète

# expectation
## discrete expectation
def expectation(X, p):
    """
    X: list of values of the random variable
    p: list of probabilities of the random variable
    """
    return sum([X[i] * p[i] for i in range(len(X))])

# variance
## discrete variance
def variance(X, p):
    """
    X: list of values of the random variable
    p: list of probabilities of the random variable
    """
    return sum([((X[i] - expectation(X, p))**2) * p[i] for i in range(len(X))])

# standard deviation
def standard_deviation(X, p):
    return variance(X, p)**0.5

# covariance
## sumi sumj (xi - E(X))(yj - E(Y)) * p(xi, yj)
def covariance(X, Y, P):
    return sum([(X[i] - expectation(X, P)) * (Y[i] - expectation(Y, P)) * P[i] for i in range(len(X))])
    
    
    
# correlation
## p(X, Y) = cov(X, Y) / (std(X) * std(Y))
def correlation(X, Y, P):
    return covariance(X, Y, P) / (variance(X, P) * variance(Y, P))


## test 
X = [1, 2, 3, 4, 5, 6]
P = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
print("expectation = " , str(expectation(X, P)))
print("variance = ", str(variance(X, P)))
print("standard deviation = " + str(standard_deviation(X, P)))
