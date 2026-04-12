class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        map_s = {}
        map_t = {}

        for char_s in s :
            map_s[char_s] = map_s.get(char_s, 0) + 1

        for char_t in t:
            map_t[char_t] = map_t.get(char_t, 0) + 1
        
        return map_s == map_t
