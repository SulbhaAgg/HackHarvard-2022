import math
from math import pi
from math import sqrt
def Perimeter(a,b):
    perimeter = 0
    perimeter = (2*pi*sqrt(((a/2)**2+(b/2)**2)/2))
    return perimeter

def getSize( underBreast, breast ):
    diff = math.floor(breast) - math.floor(underBreast)
    print(diff)
    cup = [ 'AAA' , 'AA' , 'A' , 'B' , 'C' , 'D' , 'DD' , 'DDD' , 'E' , 'F' , 'FF'
    , 'GG' , 'H' , 'HH' , 'J' , 'JJ' , 'K' , 'KK' , 'L' , 'LL' , 'M' , 'MM' , 'N' , 'O' , 'OO' , 'R' ]
    return underBreast, cup[diff+1]
if __name__=="__main__":
    d1= Perimeter(10.77/2,5.36/2)
    d2= Perimeter(13.71/2, 8.97/2)
    print(d2)
    a,b = getSize(d1,d2)
    print(a)
    print(b)