
import unittest  
class TestingSum(unittest.TestCase):  
  
    def test_sum(self):  
        self.assertEqual(sum([2, 3, 5]), 10, "It should be 10")  
    def test_sum_tuple(self):  
        self.assertEqual(sum((1, 1, 8)), 10, "It should be 10")
    def test_sum_tuple(self):  
        self.assertEqual(sum((2, 2, 6)), 10, "It should be 10")
    # def test_sum_tuple(self):  
    #    self.assertEqual(sum((1, 2, 5)), 10, "It should be 10")  
  
if __name__ == '__main__':  
    unittest.main() 
