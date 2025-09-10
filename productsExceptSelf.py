#second try. Time complexity O(n) 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        preProd = 1
        suffixProd = 1
        for num in nums:
            output.append(preProd)
            preProd*=num
        for i in range(len(output)-1, -1, -1):
            output[i] *= suffixProd
            suffixProd *= nums[i]
        return output
            
