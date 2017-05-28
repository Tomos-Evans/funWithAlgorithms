
# This function is to build a lookup table of the number of each letters that are
# available to use
def buildDict(string):
    dic = {}
    for l in string:
        if (l not in dic):
            dic[l] = 1
        else:
            dic[l] = (dic[l] + 1)
    return dic


# This solution is O(n + m) where n is the length of the target string and m
# is the length of the useable letters
def firstSolution(wantToMake, makeFrom):
    if (len(wantToMake) > len(makeFrom)):
        return False

    dic = buildDict(makeFrom)

    for l in wantToMake:
        if ((l not in dic) or (dic[l] <= 0)):
            return False
        dic[l] = (dic[l] - 1)
    return True


if __name__ == "__main__":
    wantToMake = "This is the string that we want to make"
    makeFrom   = "This is the string that we want to make the other string from"

    canBeMade = firstSolution(wantToMake, makeFrom)
    print(canBeMade)
