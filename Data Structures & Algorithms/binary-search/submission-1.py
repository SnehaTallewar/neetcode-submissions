class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_ele=0
        max_ele=len(nums)-1
        for i in range(len(nums)):
            if target== nums[min_ele]:
                return i
            elif target == nums[max_ele]:
                return max_ele
            mid = (min_ele+max_ele)/2
            if target==mid:
                return mid
            else:
                min_ele+=1
                max_ele-=1
        return -1
            
        
    
        