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

# covariance
## sumi sumj (xi - E(X))(yj - E(Y)) * p(xi, yj)
def covariance(X, Y, P): 
    pass

# correlation
## p(X, Y) = cov(X, Y) / (std(X) * std(Y))
def correlation(X, Y, P):
    pass


## test 
X = [1, 2, 3, 4, 5, 6]
P = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
print(expectation(X, P))
print(variance(X, P))
print(covariance(X, X, P))
print(correlation(X, X, P))
