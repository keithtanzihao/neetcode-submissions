class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        store = {v: i for i, v in enumerate(nums)} 

        for i in range(len(nums)):
            val2 = target - nums[i]
            
            if val2 in nums and i != store[val2]:
                return[i, store[val2]]

            

        # Too slow i guess this is technically maybe 
        # result = []
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return result.extend([i, j])
                    
            
            
