import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    #max_list
    def test_max_list_iter(self):
        """Checks basic function of max_list"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([3, 6, 9]), 9) #max value last between 3 values
        self.assertEqual(max_list_iter([35, 90, 60]), 90) #max value middle between 3 values
        self.assertEqual(max_list_iter([100, 20, 10]), 100) #max value first between 3 values
        self.assertEqual(max_list_iter([-100, -200, -300]), -100) #testing with negative numbers

        self.assertEqual(max_list_iter([4, 4, 2]), 4) #Testing repeated values in list
        self.assertEqual(max_list_iter([5, 6, 6]), 6) #Testing repeated values in different places
        self.assertEqual(max_list_iter([10, 4, 10]), 10) #Testing repeated values in different places

        self.assertEqual(max_list_iter([1, 1, 1]), 1) #Testing repeated values 
        self.assertEqual(max_list_iter([-10, -10, -10]), -10) #Testing repeated values 

        self.assertEqual(max_list_iter([]), None) #Testing empty list

        self.assertEqual(max_list_iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10) #Longer list

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError): #Test if function raises error for a None list
            reverse_rec(tlist)

        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1]) #Test with a regular positive numbers

        self.assertEqual(reverse_rec([-5, -15, 10]), [10, -15, -5]) #Test with negative numbers

        self.assertEqual(reverse_rec([1, 1, 1]), [1, 1, 1]) #Test with same numbers

        self.assertEqual(reverse_rec([100]), [100]) #Test for 1 number in list

        self.assertEqual(reverse_rec([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1]) #Test for longer list

        self.assertEqual(reverse_rec([]), []) #Empty list

    def test_bin_search(self):
        list_val = [0,1,2,3,4,7,8,9,10]
        list_val2 = [5, 10, 15, 20, 25, 30]
        list_val3 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        low = 0
        high = len(list_val)-1

        tlist = None
        with self.assertRaises(ValueError): #Test if function raises error for a None list
            bin_search(5, low, high, tlist)

        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) #Testing normal case in middle

        self.assertEqual(bin_search(8, 2, 4, list_val), None ) #Testing with random high low values that do not contain target

        self.assertEqual(bin_search(2, 1, 7, list_val), 2 ) #Testing with random high low values containing target
        self.assertEqual(bin_search(25, 2, 4, list_val2), 4 ) #Testing with random high low values containing target
        self.assertEqual(bin_search(10, 0, 4, list_val2), 1 ) #Testing with random high low values containing target

        self.assertEqual(bin_search(5, 0, 3, list_val2), 0 ) #Test number at beginning of list
        self.assertEqual(bin_search(30, 0, len(list_val2)-1, list_val2), 5 ) #Test number at the end of list

        self.assertEqual(bin_search(100, 0, len(list_val2)-1, list_val2), None ) #Test number not in list
        self.assertEqual(bin_search(10, 4, 0, list_val2), None ) #If low is greater than high

        self.assertEqual(bin_search(16, 6, 8, list_val3), 7 ) #Test if target is in upper portion of list
        self.assertEqual(bin_search(8, 1, 5, list_val3), 3 ) #Test if target is in lower portion of list
        self.assertEqual(bin_search(12, 2, 8, list_val3), 5 ) #Test in the middle of the list

        self.assertEqual(bin_search(12, 2, 8, []), None ) #Empty list


if __name__ == "__main__":
        unittest.main()

    
