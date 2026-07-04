
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        mlen = 0
        for num in nums:
            if num - 1 not in nums:
                j = num + 1
                seq_len = 1
                mlen = max(mlen, seq_len)

                while j in nums:
                    j += 1
                    seq_len += 1
                    mlen = max(mlen, seq_len)

        return mlen
                

                
        