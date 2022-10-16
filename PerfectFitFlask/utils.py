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
    return math.floor(underBreast), cup[diff+1]
def sizechart(distanceW, distanceL):
    if distanceW <= 15 and distanceL <= 26:
        size = "XXS"
    elif distanceW <= 17 and distanceL <= 27:
        size = "XS"
    elif distanceW <= 18 and distanceL <= 28:
        size = "S"
    elif distanceW <= 20 and distanceL <= 29:
        size = "M"
    elif distanceW <= 22 and distanceL <= 30:
        size = "L"
    elif distanceW <= 24 and distanceL <= 31:
        size = "XL"
    elif distanceW <= 26 and distanceL <= 32:
        size = "XXL"
    elif distanceW <= 28 and distanceL <= 33:
        size = "3XL"
    return size

def sizechartP(Perimeter):
    if Perimeter >=26 and Perimeter <=27:
        size = "XXS"
    elif Perimeter >=27 and Perimeter <=29:
        size = "XS"
    elif Perimeter >=29 and Perimeter <=31:
        size = "S"
    elif Perimeter >=31 and Perimeter <=33:
        size = "M"
    elif Perimeter >=34 and Perimeter <=36:
        size = "L"
    elif Perimeter >=36 and Perimeter <=39:
        size = "XL"
    elif Perimeter >=40 and Perimeter <=43:
        size = "XXL"
    elif Perimeter >=44 and Perimeter <=49:
        size = "3XL"
    return size
if __name__=="__main__":
    d1= Perimeter(10.77/2,5.36/2)
    d2= Perimeter(13.71/2, 8.97/2)
    print(d2)
    a,b = getSize(d1,d2)
    print(a)
    print(b)
