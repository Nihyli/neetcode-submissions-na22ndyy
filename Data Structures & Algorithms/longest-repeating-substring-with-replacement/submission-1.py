class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window
        l moves when sliding window size - max freq of letters > k
        l moves right and subratcts for hashmap
        """
        l = 0
        freqCheck = {}
        output = 0
        
        for r in range(len(s)):
            freqCheck[s[r]] = 1 + freqCheck.get(s[r], 0)

            while (r-l+1) - max(freqCheck.values()) > k:
                freqCheck[s[l]] -= 1
                l += 1
            output = max(output, r-l+1)

        return output

