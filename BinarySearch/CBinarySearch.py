import math

class CBinarySearch:
    
    def BSearch(self, nums:list[int], target:int) -> int :
        
        res = -1
        
        if not list:
            return res
        
        L, R = 0, len(nums) -1
        
        while L <= R:
            mid = math.floor((L+R)/2)
            mid_elm = nums[mid]
            
            if mid_elm == target:
                return mid
            
            if mid_elm < target:
                L = mid+1
            else:
                R = mid-1
        return res
            
bs = CBinarySearch()
print(bs.BSearch([10,20,30,40,50], 0))