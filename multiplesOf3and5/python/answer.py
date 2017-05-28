

# This is the simplist solution, it is O(n) due to the iteration
# though the list, and summing the list at the end.
# However this solution has an increased memory complexity of O(n)
def firstSolution():
    number = 1000
    multiples = []

    for i in range(number):
        if (i%3==0 or i%5==0):
            multiples.append(i)

    total = sum(multiples)
    return total

# As we are only concerned with the sum of all of the multiples, it is not
# neccisary to store the `multiples` list, we can instead just add to a rolling
# total. This brings the algorithm to O(n)
# In this solution however as we are not storing the new array there is an
# increased memory complecity of O(1), which is much better
def secondSolution():
    number = 1000
    total  = 0

    for i in range(number):
        if (i%3==0 or i%5==0):
            total += i
    return total

# Assuming that the number of divisors `m` that we are checking is small when
# compared to the upper limmit number, then this algrithm is  O(n+m)
def extFirstSol(number, multiples):
    total  = 0
    for i in range(number):
        for m in multiples:
            if (i%m==0):
                total += i
                break
    return total





if __name__ == "__main__":
    sum1 = firstSolution()
    sum2 = secondSolution()
    print(sum1)
    print(sum2)

    ext1 = extFirstSol(1000, [3,5])
    print(ext1)
