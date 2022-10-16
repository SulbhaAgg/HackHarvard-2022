from cmath import sqrt
from genericpath import getsize
from weakref import ref
from xml.etree.ElementTree import PI
import cv2
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
from utils import *

wi = 3.375
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

            

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




def Get_SIze(type1,cardPoints1,linePoints,linePoints2,cardPoints2,linePoints3,linePoints4):
    if type1.lower == "bra":
        ratio = setPixelRatio(cardPoints1)
        d1_1 = pixelToInches(linePoints, ratio)
        d2_1 = pixelToInches(linePoints2, ratio)
        ratio2 = setPixelRatio(cardPoints2)
        d1_2 = pixelToInches(linePoints3, ratio2)
        d2_2 = pixelToInches(linePoints4, ratio2)
        u = Perimeter(d1_1, d1_2)
        b = Perimeter(d2_1, d2_2)
        a, s = getSize(u,b)
        print(s)
        print(a)
    elif type1.lower == "shirt":
        ratio = setPixelRatio(cardPoints1)
        d1_1 = pixelToInches(linePoints, ratio)
        d2_1 = pixelToInches(linePoints2, ratio)
        a = sizechart(d1_1, d2_1)
    elif type1.lower == "pants":
        ratio = setPixelRatio(cardPoints1)
        d1_1 = pixelToInches(linePoints, ratio)
        d2_1 = pixelToInches(linePoints2, ratio)
        a = sizechartP(Perimeter(d1_1,d2_1))

    return a, s
if __name__=="__main__":  
    Get_SIze()     