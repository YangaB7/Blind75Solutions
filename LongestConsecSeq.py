#first attempt time complexity O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        count = 0

        # a array
        def checkNext(num, a, count):
            if num+1 in a:
                #why return
                return checkNext(num+1, a, count + 1)
            else:
                return count

        for num in mySet:
            if num - 1 in mySet:
                continue 
            else: 
                count = max(count, checkNext(num, mySet, 1))

        return count

            
