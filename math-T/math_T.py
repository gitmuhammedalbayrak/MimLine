def mimLine(name, inEnd=1, outEnd=1, inDimension=2, outDimension=2):
    name = name
    centerArray = [1]
    info=f"""
    name = {name}
    
    inEnd = {inEnd}
    outEnd = {outEnd}
    
    inDimension = {inDimension}
    outDimension = {outDimension}
    """
    print(info)

    for i in range(1, inEnd+1):
        value = -(i+1)
        centerArray.append(value)
    centerArray.sort()

    for i in range(outEnd):
        centerArray.append(i+2)
    centerArray.sort()

    print(' '.join(str(i) for i in centerArray))
    
    d_centerArray = centerArray
    merkez = d_centerArray.index(1)
    for i in range(inEnd+1):
        d_centerArray[merkez-i] = [i for i in range(inDimension)]

    for i in range(outEnd+1):
        d_centerArray[merkez+i] = [i for i in range(outDimension)]

    print(' '.join(str(i) for i in d_centerArray))



mimLine("kapi", inEnd=3, outEnd=5)
mimLine("deve", inEnd=1, outEnd=4, inDimension=2, outDimension=6)
