#assisted solution | Time Complex O(n^2), Space O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            target = -nums[i]
            p1 = i+1
            p2 = len(nums) - 1
            while p1 < p2:
                currentSum = nums[p1] + nums[p2]
                if currentSum < target:
                    p1 += 1
                elif currentSum > target: 
                    p2 -= 1
                else:
                    output.append([nums[i], nums[p1], nums[p2]])
                    p1+=1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1+=1

                    p2-=1
                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2-=1

            
        return output
