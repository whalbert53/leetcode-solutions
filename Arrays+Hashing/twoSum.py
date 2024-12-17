class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in idxmap:
                return [min(i, idxmap[complement]), max(i, idxmap[complement])]
            else:
                idxmap[nums[i]] = i
                # Dict where key=num and value=index