"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""
class Solution:
    def reverse(self, x: int) -> int:
      list_x = list(str(x))
      if x > 0:
        list_x[:] = list_x[::-1] # Reverse normla
      else:
        list_x[1:] = list_x[::-1] # Reverse everything but sign
        list_x.pop(-1) # remove excess sign form the back
      value = int(''.join(list_x)) # List to int
      if value > 2**31 - 1 or value < -2**31: # Check boundaries
        return 0 # Return 0 if exceeds boundaries
      return value