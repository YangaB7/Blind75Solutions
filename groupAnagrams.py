class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        solution = []
        for word in strs:
            currWordCount = [0] * 26
            for c in word:
                currWordCount[ord(c.lower())-ord('a')] += 1
            currWordCount = tuple(currWordCount)
            if currWordCount in answer:
                answer[currWordCount].append(word)
            else:
                answer[currWordCount] = [word]

        return list(answer.values())
