class MimLine:
    def __init__(self, name, inEnd=1, outEnd=1, inDimension=2, outDimension=2):
        self.name = name
        self.centerArray = [1]
        self.info=f"""
        name = {name}
        inEnd = {inEnd}
        outEnd = {outEnd}
        inDimension = {inDimension}
        outDimension = {outDimension}
        """
        print(self.info)

        for i in range(1, inEnd+1):
            value = -(i+1)
            self.centerArray.append(value)
        self.centerArray.sort()

        for i in range(outEnd):
            self.centerArray.append(i+2)
        self.centerArray.sort()

        self.d_centerArray = self.centerArray.copy()
        merkez = self.d_centerArray.index(1)
        for i in range(inEnd+1):
            self.d_centerArray[merkez-i] = [i for i in range(inDimension)]

        for i in range(outEnd+1):
            self.d_centerArray[merkez+i] = [i for i in range(outDimension)]


# Örnek kullanım
mim_line = MimLine("Su", inEnd=2, outEnd=2, inDimension=3, outDimension=3)
print(mim_line.centerArray)
print(mim_line.d_centerArray)