class MyInt:
    def __init__(self, value):
        self.value = value
    
    def isPrime(self):
        if self.value == 1 or self.value <1:
            return False
        for i in range(2,self.value):
            if self.value % i == 0:
                return False
        return True
    
    def showPrime(self):
        if self.value > 2:
            for i in range(2,self.value+1):
                if MyInt(i).isPrime():
                    print(i,end=" ")
            print("")
        else:
            print("!!!A prime number is a natural number greater than 1")
    
    def __sub__(self,other):
        return self.value - other.value//2
    

print(" *** class MyInt ***")
num = input("Enter 2 number : ").split()
num1 = MyInt(int(num[0]))
num2 = MyInt(int(num[1]))

print(f'{num[0]} isPrime : {num1.isPrime()}')
print(f'{num[1]} isPrime : {num2.isPrime()}')

print("Prime number between 2 and {0:d} :".format(num1.value),end=" ")
num1.showPrime()
print("Prime number between 2 and {0:d} :".format(num2.value),end=" ")
num2.showPrime()

print(f'{num1.value} - {num2.value} = {num1.__sub__(num2)}')