from queue import LifoQueue
from collections import Counter, deque

class CStack:
    def isValid(self, s: str) -> bool:
        
        paranth_stk = LifoQueue()
        
        for chr in s:
            
            if chr == "{" or chr == "(" or chr == "[":
                paranth_stk.put(chr)
            else:
                
                if paranth_stk.qsize() == 0:
                    top = ""
                else:
                    top = paranth_stk.get()
                
                if (chr == "}" and top == "{") or (chr == ")" and top == "(") or (chr == "]" and top == "["):
                    pass
                else:
                    return False
        
        return paranth_stk.empty()
    
    def evalRPN(self, tokens: list[str]) -> int:
        oprnd_stk = deque()
        
        for each_token in tokens:

            if each_token == '+' or each_token == '-' or each_token == '*' or each_token == '/':
                #we found an operator    
                match each_token:
                    case '+':
                       oprnd_stk.append(int(oprnd_stk.pop() + oprnd_stk.pop()))                       
                    case '-':
                        a,b = oprnd_stk.pop(), oprnd_stk.pop()                         
                        oprnd_stk.append(int(b - a))
                    case '*':
                        oprnd_stk.append(int(oprnd_stk.pop() * oprnd_stk.pop()))
                    case '/':
                        a,b = oprnd_stk.pop(), oprnd_stk.pop() 
                        oprnd_stk.append(int(b / a))
            else:
                oprnd_stk.append(int(each_token))

        return oprnd_stk.pop()         
      
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack( openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
    
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        res = [0]*len(temperatures)
        
        stk = deque()
        
        for i, elem in enumerate(temperatures):
            
            while stk.__len__() > 0 and elem > stk[-1][0]:
                pair = stk.pop()
                res[pair[1]] = i - pair[1]
            
            stk.append(tuple([elem, i]))
            
        return res    
    
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        hmap = dict() 
        car_fleet = len(position)
            
        #map pos of car vs time taken by each car into the map
        time_of_cars = []
        for i in range(len(position)):
            time_of_cars.append((target - position[i]) / speed[i])    
            hmap[position[i]] = time_of_cars[i]
        
        #sort the positions list. so we can start from the car at the beginning of the lane.
        position = sorted(position)
        
        i = len(position)-1
        
        while i >= 0:            
            #starting from the rev, car with position val - high
            
            time_taken_by_ith_car = hmap[position[i]]
            i -= 1
            
            while i >= 0 and time_taken_by_ith_car >= hmap[position[i]]:  
                car_fleet -= 1
                i -= 1

        return car_fleet

    def largestRectangleArea(self, heights: list[int]) -> int:
        
        MaxArea = 0
        stk = deque()
        
        for i, h in enumerate(heights):
            
            start_indx = i
            while stk and stk[-1][1] > h:
                curr_indx, curr_h = stk.pop()
                MaxArea = max(MaxArea, (curr_h * (i - curr_indx)))
                start_indx = curr_indx
            
            stk.append(tuple([start_indx,h]))
            
        for i,h in stk:
            curr_area = h[1] * (len(heights) - i)
            MaxArea = max(MaxArea, curr_area)
            
        return MaxArea
            
s = CStack()
s.largestRectangleArea([2,1,5,6,2,3])



class MinStack:

    def __init__(self):
        self.stk = deque()

    def push(self, val: int) -> None:
        if self.stk.__len__() > 0:
            stk_curr_min = self.stk[-1][1]
            actual_min = min(stk_curr_min, val)           
            val_currmin_pair = tuple([val, actual_min])
        else:
            val_currmin_pair = tuple([val, val])
 
        self.stk.append(val_currmin_pair)

    def pop(self) -> None:
        if self.stk.__len__() > 0:
            val = self.stk.pop()

    def top(self) -> int:
        if self.stk.__len__() > 0:
            val = self.stk[-1][0]
            return val

    def getMin(self) -> int:
        if self.stk.__len__() > 0:
            min = self.stk[-1][1]
            return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()