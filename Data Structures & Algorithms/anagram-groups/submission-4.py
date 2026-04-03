class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashCheck = {}

        for word in strs:
            sort = "".join(sorted(word))

            if sort not in hashCheck:
                hashCheck[sort] = []
            
            hashCheck[sort].append(word)
        
        return list(hashCheck.values()) 
        