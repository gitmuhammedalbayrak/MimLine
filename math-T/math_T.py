import random

class MimLine:
    def __init__(self, name, inEnd=1, outEnd=1, inDimension=2, outDimension=2):
        self.name = name
        self.centerArray = [1]
        self.info = f"""
        name = {name}
        inEnd = {inEnd}
        outEnd = {outEnd}
        inDimension = {inDimension}
        outDimension = {outDimension}
        """
        self.initialize_center_array(inEnd, outEnd, inDimension, outDimension)
        self.initialize_dimensional_center_array(inEnd, outEnd, inDimension, outDimension)
        self.add_zeros()
        self.display()

    def initialize_center_array(self, inEnd, outEnd, inDimension, outDimension):
        for i in range(1, inEnd + 1):
            value = -(i + 1)
            self.centerArray.append(value)
        self.centerArray.sort()

        for i in range(outEnd):
            self.centerArray.append(i + 2)
        self.centerArray.sort()

    def initialize_dimensional_center_array(self, inEnd, outEnd, inDimension, outDimension):
        self.dimensional_centerArray = self.centerArray.copy()
        merkez = self.dimensional_centerArray.index(1)
        for i in range(inEnd + 1):
            if self.dimensional_centerArray[merkez - i] != 1:
                self.dimensional_centerArray[merkez - i] = [j for j in range(inDimension)]

        for i in range(outEnd + 1):
            if self.dimensional_centerArray[merkez + i] != 1:
                self.dimensional_centerArray[merkez + i] = [j for j in range(outDimension)]

    def add_zeros(self):
        self.centerArray.insert(0, 0)
        self.centerArray.append(0)
        self.dimensional_centerArray.insert(0, 0)
        self.dimensional_centerArray.append(0)

    def display(self):
        print(f"Info: {self.info}")
        print(f"Center Array: {self.centerArray}")
        print(f"Dimensional Center Array: {self.dimensional_centerArray}")

class MimLineTest:
    def __init__(self):
        self.tests = 5000

    def run_tests(self):
        for i in range(self.tests):
            print(f"--- Test {i+1} ---")
            inEnd = random.randint(1, 10)
            outEnd = random.randint(1, 10)
            inDimension = random.randint(1, 10)
            outDimension = random.randint(1, 10)
            line = MimLine(f"Example{i+1}", inEnd, outEnd, inDimension, outDimension)
            self.test_mimline(line)
            print()

    def test_mimline(self, line):
        # Başında ve sonunda sıfır olup olmadığını kontrol etme
        if line.centerArray[0] == 0 and line.centerArray[-1] == 0:
            print("Başında ve sonunda sıfır var.")
        else:
            raise ValueError("Başında veya sonunda sıfır yok.")

        # Liste içinde 1 değerinin olup olmadığını kontrol etme
        if 1 in line.dimensional_centerArray:
            print("Listede 1 değeri mevcut.")
        else:
            raise ValueError("Listede 1 değeri yok veya değiştirilmiş.")


# MimLineTest sınıfı kullanarak testleri çalıştırma
test = MimLineTest()
test.run_tests()