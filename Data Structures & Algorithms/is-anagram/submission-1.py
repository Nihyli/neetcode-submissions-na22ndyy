class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s = 'racecar'
        t = 'carrace'

        charDictionaryS 
        charDictionaryT

        for loop len(s)
        if char not in hashmap we add else we incrememnt by one

        charDictionaryS == charDictionaryT
        return True
        """

        charDictionaryS = {}
        charDictionaryT = {}

        for char in s:
            if char not in charDictionaryS:
                charDictionaryS[char] = 0
            charDictionaryS[char] += 1
        
        for char in t:
            if char not in charDictionaryT:
                charDictionaryT[char] = 0
            charDictionaryT[char] += 1

        return charDictionaryS == charDictionaryT

        