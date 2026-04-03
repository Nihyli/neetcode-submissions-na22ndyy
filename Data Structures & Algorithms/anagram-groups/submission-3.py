class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = {}
        returnList = []

        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord not in hash1:
                hash1[sortedWord] = []
            hash1[sortedWord].append(word)
        
        for k, v in hash1.items():
            returnList.append(v)
        
        return returnList
        

        