if __name__ == '__main__':
    a = 1
    
    b = 11
    b = 'see: {}'
    print (b)
    print(b.format(23))
    
    
    c = 'Number in binary: {:b}'
    print (c.format(23))
    
    a = [3,7,2,1]
    print (a)
    print (len(a))
    print (list(reversed(a)))
    
    a.pop()
    print (a)
    a.append (13)
    print (a)
    
    def convertBinaryToDecimal(binaryList):
        binaryList = list(reversed(binaryList))
        result = 0
        while len(binaryList) > 0:
            result = result + binaryList.pop()
            result = result * 2
        return result//2
    
    print(convertBinaryToDecimal([1,1,1,1,1]))
    
    def convertDecimalToBinary(n):
        if n > 0:
            binaryList = []
            while n > 0:
                if n % 2 == 0:
                    binaryList.append(0)
                else:
                    binaryList.append(1)
                n = n // 2
            return list(reversed(binaryList))
        elif n == 0:
            return [0]
        else:
            return Exception("No negative values allowed")
        
    print (convertDecimalToBinary(10))