# MimLine

MimLine is an example of a bipolar and multi-dimensional number sequence, where "0" is at the beginning and the end of the sequence, with "1" at the center. In this sequence, "1" is centrally located, with its positive neighbor being "2" and its negative neighbor being "-2". The number "-1" is not present in the sequence but is conceptually positioned in a vertical sub-space: remember, this is purely conceptual.

The negative space represents the essence or inner content of a numerical object, while the positive space represents its scope or encompassing elements. In scope and essence, each layer represents a different dimension, with each dimension containing its own levels.

For example:
An apple = "1"
The first-degree essence of the apple (which always represents the sum of all content of the object) = -2
The second-degree essence of the apple (e.g., its essence in the context of physics) = -3

For the dimension example, if we take -3 (again using the apple):
[-3[0,1]] = Here, we see that it is analyzed in two parts physically. For these two numbers, we can give the following examples:
0 = its mass
1 = its speed

The positive aspect will be explained later.

## Features

- `name`: Represents the name of the example.
- `centerArray`: Holds an array referred to as the central array.
- `dimensional_centerArray`: Holds a dimensional central array.

## Installation

No additional installation is required. You can use the code directly.

## Usage

The following example demonstrates how to use the MimLine class:

```python
# Example usage
line = MimLine("Example", inEnd=2, outEnd=1, inDimension=3, outDimension=2)
line.display()
```

## Tests

Tests have been created to verify the correct functioning of the MimLine class. The following code example includes the MimLineTest class, which will run 5000 tests:

```python
import random

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
        # Check if there is a zero at the beginning and end
        if line.centerArray[0] == 0 and line.centerArray[-1] == 0:
            print("Zero is at the beginning and end.")
        else:
            raise ValueError("There is no zero at the beginning or end.")

        # Check if the value 1 is present in the list
        if 1 in line.dimensional_centerArray:
            print("The value 1 is present in the list.")
        else:
            raise ValueError("The value 1 is not in the list or has been altered.")
```

### Running Tests with the MimLineTest Class
```python
test = MimLineTest()
test.run_tests()
```

Errors resulting from the tests will be shown by raising a ValueError. If the tests pass successfully, no output will be produced.

## License

This project is licensed under the T1 License. To obtain the license or for more information, please contact me directly. If I am not reachable, it should be considered that no license has been granted.
