from cmath import sqrt
from weakref import ref
import cv2
from tabulate import tabulate
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
cardPoints = []
linePoints = []
ref1 = []
clickNum = 0
wi = 3.375
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def click_event(event, x, y, flags, params):
     
        if event == cv2.EVENT_LBUTTONDOWN:
            
            ref0 = []
            global ref1
            ref0.append(x)
            ref0.append(y)
            ref1.append(ref0)
            print(ref1)
            global clickNum, linePoints, cardPoints
            if(clickNum>=0 and clickNum<4):
                cardPoints.append(ref0)
            elif(clickNum>=4 and clickNum<6):
                linePoints.append(ref0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(resized_down,'.',(x,y), font, 1, (255,20,147), 10)
            if clickNum != 0:
                cv2.line(resized_down, ref1[clickNum-1], (x,y), (255,20,147), 10)
            clickNum+=1
            

            cv2.imshow('image', resized_down)
            

def setPixelRatio(cardPts):
    W1_px=sqrt((cardPts[0][0]-cardPts[1][0])**2+(cardPts[0][1]-cardPts[1][1])**2)#sqrt((x0-x1)^2-(y0-y1)^2)
    H1_px=sqrt((cardPts[1][0]-cardPts[2][0])**2+(cardPts[1][1]-cardPts[2][1])**2)
    W2_px=sqrt((cardPts[2][0]-cardPts[3][0])**2+(cardPts[2][1]-cardPts[3][1])**2)#sqrt((x0-x1)^2-(y0-y1)^2)
    H2_px=sqrt((cardPts[3][0]-cardPts[0][0])**2+(cardPts[3][1]-cardPts[0][1])**2)
    ratio1Avg = (W1_px+W2_px)/(2*3.375) 
    ratio2Avg = (H1_px+H2_px)/(2*2.125)
    ratioAvg = (ratio1Avg+ratio2Avg)/2
    return ratioAvg


def pixelToInches(line, ratio):
    L_px=sqrt((line[0][0]-line[1][0])**2+(line[0][1]-line[1][1])**2)#sqrt((x0-x1)^2-(y0-y1)^2)
    L = L_px/ratio
    return L


if __name__=="__main__":
    print("Hello")
    # reading the image
    img = cv2.imread("imgs/1.jpg", cv2.IMREAD_UNCHANGED)
        
     
    # displaying the image
    scale_percent = 30 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_down = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('image', resized_down)
    # setting mouse handler for the image
    # and calling the click_event() function
    
    cv2.setMouseCallback('image', click_event)
    
    
        
     
    # wait for a key to be pressed to exit
    cv2.waitKey(0)  
    print(cardPoints)
    ratio = setPixelRatio(cardPoints)
    distance = pixelToInches(linePoints, ratio)
     
    

    print(distance)

        
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()

def sizechart(distanceW, distanceL):
    table = [['Mens T-Shirt Size', 'Width(inches)', 'Lenght(inches)'], ['XXS', 15, 26], ['XS', 17, 27], ['S',18, 28],  ['M', 20, 29], ['L', 22, 30], ['XL', 24, 31],['XXL', 26, 32],['3XL', 28, 33]]
    print(tabulate(table, tablefmt='fancy_grid'))
    size = "Values are innacurate"
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
