


# This is the most obvious solution, but with its O(n^2) time complexity
# it is not an acceptable solution
def firstSolution(array, desiredSum):
    for i in range(len(array)):
        for j in range(len(array)):
            if ((i!=j) and (array[i] + array[j] == desiredSum)):
                return True
    return False


# This slight adaption of the first solution is marginly better as it does not
# repeat comparisons, however it is still O(n^2)
def secondSolution(array, desiredSum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if ((i!=j) and (array[i] + array[j] == desiredSum)):
                return True
    return False


# This solution is much better as it leverages a bidirectional system
# As the array is ordered, if the sum of two number is too big, then the only
# way to make it smaller is to move in the rightmost checker and visa-versa.
# As this algorithm only steps though each element of the list at most once
# it is O(n)
def thirdSolution(array, desiredSum):
    i = 0
    j = len(array) - 1
    while(i < j):
        summed = array[i]+array[j]
        if (summed == desiredSum):
            return True
        elif(summed > desiredSum):
            j -=1
        elif(summed < desiredSum):
            i +=1
    return False


def extFirstSolution(array, desiredSum):
    seen = []                                                                   # TODO This should be a hashmap for O(1) lookup
    for elem in array:
        comp = desiredSum - elem
        if (comp in seen):
            return True
        seen.append(elem)
    return False



if __name__ == "__main__":
    answer = thirdSolution([1,2,4,4,5], 8)
    extAns = extFirstSolution([1,1,3,2,4], 8)

    print(answer)
    print(extAns)
