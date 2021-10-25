
import unittest  
class TestingSum(unittest.TestCase):  
  
    def test_sum(self):  
        self.assertEqual(sum([2, 3, 5]), 10, "It should be 10")  
    def test_sum_tuple(self):  
       self.assertEqual(sum((1, 3, 5)), 10, "It should be 10")
    def test_sum_tuple(self):  
       self.assertEqual(sum((1, 1, 5)), 10, "It should be 10")
    def test_sum_tuple(self):  
       self.assertEqual(sum((1, 2, 5)), 10, "It should be 10")  
  
if __name__ == '__main__':  
    unittest.main() 

# import unittest

# class TestsContainer(unittest.TestCase):
#     longMessage = True

#     testsmap = {
#         'foo': [1, 1],
#         'bar': [1, 2],
#         'baz': [5, 5],
#         'baf': [5, 6],
#     }

#     def test_a(self):
#         for name, (a, b) in self.testsmap.items():
#             with self.subTest(name=name):
#                 self.assertEqual(a, b, name)

# if __name__ == '__main__':
#     unittest.main()
