import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_eq(self):
    	loc1 = Location("LA", 3.3, -4.3)
    	loc2 = Location("Virginia", 9.91, 4.56)
    	loc3 = Location("LA", 3.3, -4.3)
    	self.assertEqual(loc1 == loc3, True)
    	self.assertEqual(loc2 == loc3, False)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
