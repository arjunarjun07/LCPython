class CRecursion:
    
    def fibonocciofn(self,n:int) -> int:
        res = -1
        hmap = {}
        
        def fibo(n):
            
            if n <= 1:
                if n not in hmap.keys():
                    hmap[n] = n
                return hmap[n]          
            else:
                if n-1 not in hmap.keys():
                    hmap[n-1] = fibo(n-1)
                
                if n-2 not in hmap.keys():
                    hmap[n-2] = fibo(n-2)
                    
                hmap[n] = hmap[n-1] + hmap[n-2]
                
                return hmap[n]
        res = fibo(n)
        return res
    
    """
        print_n_natural_nums()

        f(n) = 
                {
                    None ; n = 0
                    
                    f(n-1) ; n >0
                }
    """
    
    def print_n_natural_nums(self, n:int):
        if n > 0:
            self.print_n_natural_nums(n-1)
            print(n)
    
    """
        sum_of_n()
        
        f(n) = 
                {
                    n           ; n >=1

                    n + f(n-1)  ; n > 1
                }
    """
    
    def sum_of_n_nums(self, n:int) -> int:
        
        if n <= 0:
            return n
        else:
            return n + self.sum_of_n_nums(n-1)  
        
    """
        count_digits()
        
        f(n) = 
                {
                    1       ;   n < 10
                    1 + f(n/10) ; n >= 10
                }
    """
    
    def count_digits(self, n:int)-> int:
        
        if n < 10:
            return 1
        else:
            return 1 + self.count_digits(n//10)
        
    """
        sum_of_digits()
        
        f(n) = 
                {
                    n       ;       n < 10
                    
                    (n % 10) + f(n/10) ;   n >= 10
                }
    """ 
    
    def sum_of_digits(self, n:int)->int:
        
        if n < 10:
            return n
        else:
            return (n%10) + self.sum_of_digits(n//10)
        
    """
        RaisePower(num, p)
        
        f(n) = 
                {
                    1               ;       p = 0
                    num             ;       p = 1
                    num * f(n, p-1) ;       p > 1
                }
    """
    def raise_power(self, num:int, pow:int) -> int:
        
        if pow == 0:
            return 1
        elif pow == 1:
            return num
        else:
            return num * self.raise_power(num, pow-1)

    
    def convert_binary(self, num:int) -> str:
        binary_str = []
        ans = ""
        def binary(num):
            
            if num >= 0:         
                if num <= 1:
                    binary_str.append(num)
                else:
                    binary(num//2)
                    binary_str.append(num % 2)
        
        binary(num)   
        ans = ''.join(map(str, binary_str))
               
        return ans
    
    """
        isprime()
        
        f(n) = 
                {
                    false    ;       n <= 1
                    false    ;       n % divisor == 0 & i !=1
                    
                    true     ;       i == 1
                    f(num, divisor+1)   ;   i > 1 
                }
    """
    
    def IsPrime(self, num:int) -> bool:
        
        i = num - 1
        
        def FindPrime(num, i:int):
            if num <= 1 or (i != 1 and num % i == 0):
                return False

            if i == 1:
                return True
            else:
                return FindPrime(num, i-1)
        
    def GCD(self, a:int, b:int)-> int:
        #Euclidian subraction
        
        # Everything divides 0
        if (a == 0):
            return b
        if (b == 0):
            return a

        # base case
        if (a == b):
            return a

        # a is greater
        if (a > b):
            return self.GCD(a-b, b)
        return self.GCD(a, b-a)
      
 
c = CRecursion()
print(c.GCD(15, 13))

# bool IsPrime(int num, int divisor);
# int GCD(int a, int b);