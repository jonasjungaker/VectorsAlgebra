import unittest
from vector import *

class vectorTester(unittest.TestCase):
    def testAssignment(self):
        v1 = vector(1, 1)
        v2 = vector(1, 1)
        self.assertEqual(v1, v2)

        v1[0] = 2
        self.assertEqual(vector(2, 1), v1)

        v1[0] = v1[0] + 1
        self.assertEqual(vector(3, 1), v1)

        self.assertEqual(1, v1[1])

        v1 = vector(1, 2, 3, 4)
        self.assertEqual(v1[3], 4)

    def testAddition(self):
        v1 = vector(1, 2)
        v2 = vector(2, 4)
        v3 = v1 + v2
        self.assertEqual(vector(3, 6), v3)
        self.assertEqual(vector(6, 12), v3 + v3)

    def testDotProduct(self):
        v1 = vector(2, 3)
        v2 = vector(3, 4)
        self.assertEqual(v1 * v2, 18)

    def testCrossProduct(self):
        v1 = vector(1, 2, 3)
        v2 = vector(2, 3, 4)
        v3 = vector(-1, 2, -1)
        self.assertEqual(v3, v1 @ v2)

    def testDimensionError(self):
        v1 = vector(1, 2, 3, 4)
        v2 = vector(2, 3)
        self.assertRaises(TypeError, lambda: v1 + v2)
        self.assertRaises(TypeError, lambda: v1 * v2)
        self.assertRaises(TypeError, lambda: v1 @ v2)
        
    def testMagnitude(self):
        v1 = vector(1, 1, 1)
        self.assertEqual(v1.magnitude(), 3)
        self.assertEqual(round(abs(v1), 4), round(1.7320508, 4))

    def testTypeError(self):
        self.assertRaises(TypeError, vector("a"))
    

if __name__ == "__main__":
    unittest.main()
