x = int(input("Enter the number: "))

match x:
    case 0:
        print("x is", x)
    case 4:
        print("x is", x)
    case 7:
        print("x is", x)
    # case _ :
    #     print("x is", x)
    case _ if(x>10):
        print("x is greater than 10")
    case _ if(x>20):
        print("x is greater than 20")
    case _ if(x==100):
        print("x is equal to 100")
    