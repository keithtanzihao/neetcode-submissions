class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            val2 = target - nums[i] # 3

            if val2 in store and store[val2] != i:
                return [store[val2], i]
            
            store[nums[i]] = i # 3: 0

                    
            
            
