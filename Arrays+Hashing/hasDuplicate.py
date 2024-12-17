class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # If nums has duplicates, those duplicates will be removed in the set