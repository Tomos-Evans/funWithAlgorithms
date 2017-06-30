
def isPrime(n):
    if (n < 2):
        return False
    if (n==2):
        return True
    if (n%2 == 0):
        return False
    for i in range(3, int((n**0.5)+1)):
        if (n%i ==0):
            return False
    return True


def find(nthPrime=10001):
    primesFound  = 0
    currentTry   = 0
    currentPrime = None
    while (primesFound != nthPrime):
        if (isPrime(currentTry)):
            primesFound += 1
            currentPrime = currentTry
        currentTry +=1
    return currentPrime
