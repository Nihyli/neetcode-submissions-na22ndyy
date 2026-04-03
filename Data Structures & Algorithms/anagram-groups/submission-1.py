class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        sort each word
        each uniqe sorted word is a key for dict
        value would be an empty list
        go through list
        sort each word and append it to the list that matches
        return the list version of the values
        """
        
        sortedToHash = {}
        sortedList = []

        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            sortedList.append(sortedWord)
            if sortedWord not in sortedToHash:
                sortedToHash[sortedWord] = []
            sortedToHash[sortedWord].append(strs[i])
        
        return list(sortedToHash.values())
