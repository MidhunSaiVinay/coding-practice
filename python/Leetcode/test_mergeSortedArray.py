import unittest
from mergeSortedArray import Solution

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_merge_basic(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        m, n = 3, 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,2,3,5,6])
        
    def test_merge_empty_nums2(self):
        nums1 = [1,2,3]
        nums2 = []
        m, n = 3, 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3])
        
    def test_merge_empty_nums1(self):
        nums1 = [0]
        nums2 = [1]
        m, n = 0, 1
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])
        
    def test_merge_all_smaller(self):
        nums1 = [4,5,6,0,0,0]
        nums2 = [1,2,3]
        m, n = 3, 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3,4,5,6])

if __name__ == '__main__':
    unittest.main()