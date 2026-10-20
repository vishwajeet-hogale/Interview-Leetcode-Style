class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = "".join([str(n) for n in digits])

        nums = int(nums)

        return [s for s in str(nums+1)]
        