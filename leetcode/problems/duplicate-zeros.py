class Solution(object):
  def duplicateZeros(self, arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    result = []
    should_append_zero = False
    for index in range(len(arr)):
      if should_append_zero:
        arr.insert(index, 0)
        arr.pop()
        should_append_zero = False
      elif arr[index] == 0:
        should_append_zero = True

