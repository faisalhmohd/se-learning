class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        diff = 0
        arr = self.__elements
        for i in range(len(arr)):
            for num in arr[i:]:
                # print(num, ' ', arr[i] - num)
                tmp = abs(arr[i] - num)
                if tmp > diff:
                    diff = tmp
        self.maximumDifference = diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)