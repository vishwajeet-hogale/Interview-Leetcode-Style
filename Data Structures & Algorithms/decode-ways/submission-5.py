class Solution:
    def numDecodings(self, s: str) -> int:
        hash_map = {str(i+1): chr(65 + i) for i in range(26)}
        memo = {}
        def recurse(temp_s):
            if temp_s == "":
                return 1
            
            if temp_s in memo:
                return memo[temp_s]
            choice_one_char, choice_two_char = 0, 0
            if temp_s[:1] in hash_map:
                choice_one_char = recurse(temp_s[1:])
            if len(temp_s) >= 2 and temp_s[:2] in hash_map:
                choice_two_char = recurse(temp_s[2:])
            memo[temp_s] = choice_one_char + choice_two_char
            return memo[temp_s]


        return recurse(s)
            