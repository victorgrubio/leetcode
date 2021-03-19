import unittest
from rotate_image import Solution

class TestRotateImage(unittest.TestCase):

    def test_rotate_image(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        result = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, result)

if __name__ == '__main__':
    unittest.main()