#time complexity O(m) space complexity O(m+n) 
#Where m is the sum of lengths of all the strings and n is the number of strings
class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string))+ "#" + string
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        validatingNum = True
        potentialNum = ""
        currWordLength = 0
        currWord = ""
        
        #fails if first string is "0#" EX "4#tree0#4#tree"
        for letter in s:
            #parsing word length
            if letter.isdigit() and validatingNum:
                potentialNum += letter
            #if no letter just skip
            if letter == "#" and validatingNum and int(potentialNum) == 0:
                output.append("")
                continue
            #ending parse
            if letter == "#" and validatingNum:
                validatingNum = False
                currWordLength = int(potentialNum)
                continue
            #adding letters
            if not validatingNum and currWordLength != 0:
                currWord += letter
                currWordLength -= 1
            #reset 
            if not validatingNum and currWordLength == 0:
                validatingNum = True
                potentialNum = ""
                currWordLength = 0
                output.append(currWord)
                currWord = ""
        return output

