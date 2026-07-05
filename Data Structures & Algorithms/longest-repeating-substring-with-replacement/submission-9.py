class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        c = k
        l = ans = 0
        hashmap = defaultdict(int)
        
        for r in range(n):
            hashmap[s[r]] += 1
            val = max(hashmap.values())
            while (r-l+1) - val > k:
                hashmap[s[l]] -= 1 
                l+=1
                val =  max(hashmap.values())
            ans = max(ans, (r-l+1))
        ans = max(ans, (r-l+1))
        return ans

#YYXXXY k =2 

        

           



            


