def average(a,b):
    print("the average is ", (a+b)/2)

average(4,6)

# default arguments

def average1(a=5,b=10):
    print("the average is ", (a+b)/2)
        
average1()
average1(8,16)

# keyword arguments

average1(b=30,a=56)

# required arguments

def averag(a,b=34):
    print("the average is ", (a+b)/2)

averag(a=4)

# variable arguments

def aver(*numbers):
    for i in numbers:
        sum = 0
        sum = sum + i
    print("the average is ", sum/len(numbers))

aver(40,5,6,3)