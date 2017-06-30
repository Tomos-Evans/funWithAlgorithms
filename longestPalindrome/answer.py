def iterate():
    maxPal = -1
    for i in range(100,999+1):
        for j in range(100,999+1):
            if (isPal(i*j) and (i*j > maxPal)):
                maxPal = i*j
    print(maxPal)



def isPal(number):
    string      = str(number)
    leftMarker  = 0
    rightMarker = len(string)-1

    while(leftMarker<rightMarker):
        if (string[leftMarker]!=string[rightMarker]):
            return False
        else:
            leftMarker  +=1
            rightMarker -=1
    return True
