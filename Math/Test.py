if __name__ == '__main__':
    x = 21
    if x < 10 or x > 20:
        print (42)
        
    def fakultyFn (n):
        if n == 0:
            return 1
        elif n < 0:
            return Exception("No negative arguments allowed")
        else:
            i = 1
            s = 1
            while i <= n:
                s = s * i
                i += 1
            return s
        
    print (fakultyFn(18))
        
    def dist (x,y):
        d = x-y
        if d < 0:
            d = -d
        return d
        
    a = 100
    a += 10
    print (a)
    
    i = 1
    s = 0
    while i <= 10:
        s = s + i
        i = i + 1
        print (s)
        
    def sumFn (n):
        if n >= 0:
            i = 1
            s = 0
            while i <= n:
                s = s + i
                i = i + 1
            return s
        if n < 0:
            i = -1
            s = 0
        while i >= n:
            s = s + i
            i = i - 1
        return s
    z = sumFn(0)
    print (z)
    
    
    def absValueFn (n):
        if n >= 0:
            return n
        else:
            return -n
        
    print (absValueFn(6))
    

    def greaterDistanceToZero (n,m):
        if absValueFn(n)> absValueFn(m):
            return n
        else:
            return m
    
    print (greaterDistanceToZero(19, -7))
    
    def aToThePowerOfb (a,b):
        if a == 0:
            return 0
        elif b == 0:
            return 1
        else:
            s = 1
            for i in range (b):
                s = s * a
            return s
        
        
    print (aToThePowerOfb(4,0))