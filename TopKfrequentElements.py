#solution #1 without assistance O(nlogn) time complex
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = {}
        solution = []
        for num in nums:
            if num not in answer:
                answer[num] = 1
            else:
                answer[num] += 1

        answerList = list(answer.items())
        answerList.sort(key=lambda p: p[1], reverse=True)
        
        topkpairs = answerList[:k]
        
        return [sublist[0] for sublist in topkpairs]

#solution #2 with assitance O(n) time complex
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = {}
        bucket = [[] for _ in range(len(nums) + 1)] 
        solution = []
        for num in nums:
            if num not in answer:
                answer[num] = 1
            else:
                answer[num] += 1

        for num, freq in answer.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                if len(solution) == k:
                    break
                solution.append(num)
                
        return solution
        


        
  
