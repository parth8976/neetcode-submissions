class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        # return False
        seen = {}

        for i in range(len(nums)):
            left = target - nums[i]

            if left in seen:
                return [seen[left],i]
            
            seen[nums[i]] = i
