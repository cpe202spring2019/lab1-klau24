
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
     return None
   elif int_list == None:
     raise ValueError
   max_int = int_list[0]
   
   for i in int_list:
     if i > max_int:
       max_int = i
   return max_int

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return []
   if len(int_list) == 1:
      return int_list[0:]
   return reverse_rec(int_list[1:len(int_list)]) + int_list[0:1]
    
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return None
   middle = (low + high) // 2
   if low > high:
      return None
   elif int_list[middle] == target:
      return middle 
   elif int_list[middle] > target: 
      return bin_search(target, low, middle - 1, int_list)
   else:
      return bin_search(target, middle + 1, high, int_list)





