class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]
        for index, g in enumerate(gain):
          altitudes.append(altitudes[index] + g)

        return max(altitudes)