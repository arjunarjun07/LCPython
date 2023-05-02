from collections import defaultdict, deque
import math
from functools import reduce

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
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        res = False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            
            front_elm = matrix[i][0]
            back_elm = matrix[i][-1]
            
            if front_elm <= target <= back_elm:
                #The element found in this row - we can apply binary search
                indx = self.BSearch(matrix[i], target)
                
                if indx != -1:
                    return True
                                
        return res
    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        MaxBanana = max(piles)
        
        res_eating_speed = MaxBanana

        #avg banana eating speed for all piles & given h -> (Sum of all piles / h hrs )
        #inorder to eat all bananas koko needs to eat avg_speed bananas per hr. But we need to equate to the given hrs - h
        avg_speed = int(sum(piles)/ h)
        
        #we generate the list of speed in reverse sorted order. So we can apply binary search based on results equate to h-hrs
        speed_list = list(range(avg_speed, MaxBanana+1, 1))
        
        def TotalTimeTakenforGivenSpeed(spd:int) -> int:
            res = [math.ceil(x/spd) for x in piles]
            return sum(res)
        
        L, R = 0, len(speed_list)-1
        
        while L < R:
            
            mid = math.floor((L+R)/2)
            mid_elm = speed_list[mid]
            
            time_taken_by_curr_speed = TotalTimeTakenforGivenSpeed(mid_elm)
            
            if time_taken_by_curr_speed <= h:
                res_eating_speed = min(res_eating_speed, mid_elm)
                R = mid-1
            else:
                L = mid+1
        
        return res_eating_speed
    
    def findMin(self, nums: list[int]) -> int:
        
        
        L, R = 0, len(nums)-1
        res = nums[L]
              
        while L <= R:
            
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            
            mid = (L+R)//2
            res = min(res, nums[mid])
            
            if nums[L] <= nums[mid]:
                #Left sub array is sorted. so we need to check Right sub array. move L 
                L = mid + 1
            else:
                R = mid -1
        
        return res
                      
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            # right sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1
    
    def getImmediateminiftargetnotfound(self, nums: list[int], target: int) -> int:
        L,R = 0, len(nums)-1
        
        res = -1
        
        while L <= R:
            
            mid = (L+R)//2
            
            if nums[mid] == target:
                res = nums[mid]
                print(res)
                return
            
            if nums[mid] < target:
                res = max(res, nums[mid])
                L = mid +1
            else:
                R = mid - 1
        return res
            
            
bs = CBinarySearch()
print(bs.test())

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

#["TimeMap","set","set","get","get","get","get","get"]

#[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]


# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap();

timeMap.set("love","high",10);  
timeMap.set("love","low",20);

val = timeMap.get("love",5);
val = timeMap.get("love",10);
val = timeMap.get("love",15);
val = timeMap.get("love",20);
val = timeMap.get("love",25);