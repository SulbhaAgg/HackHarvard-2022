from cmath import sqrt
import cv2
def click_event(event, x, y, flags, params):
     
        if event == cv2.EVENT_LBUTTONDOWN:
            ref0 = []
            ref1 = []
            ref0.append(x)
            ref0.append(y)
            ref1.append(ref0)
            print(ref1)


def setPixelRatio(cardPts, refL, refH):
    L1_px=sqrt((cardPts[0][0]-cardPts[1][0])**2+(cardPts[0][1]-cardPts[1][1]))#sqrt((x0-x1)^2-(y0-y1)^2)
    H1_px=sqrt((cardPts[1][0]-cardPts[2][0])**2+(cardPts[1][1]-cardPts[2][1]))
    L2_px=sqrt((cardPts[2][0]-cardPts[3][0])**2+(cardPts[2][1]-cardPts[3][1]))#sqrt((x0-x1)^2-(y0-y1)^2)
    H2_px=sqrt((cardPts[3][0]-cardPts[0][0])**2+(cardPts[3][1]-cardPts[0][1]))
    ratio1Avg = (L1_px+L2_px)/(2*refL)
    ratio2Avg = (H1_px+H2_px)/(2*refH)
    ratioAvg = (ratio1Avg+ratio2Avg)/2
    return ratioAvg


def pixelToInches(line, ratio):
    L_px=sqrt((line[0][0]-line[1][0])**2+(line[0][1]-line[1][1]))#sqrt((x0-x1)^2-(y0-y1)^2)
    L = L_px/ratio
    return L


if __name__=="__main__":
    print("Hello")
    # reading the image
    img = cv2.imread("1.jpg", 1)
        
     
    # displaying the image
    cv2.imshow('image', img)
     
    # setting mouse handler for the image
    # and calling the click_event() function
         
    cv2.setMouseCallback('image', click_event)

        
     
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
     
    # close the window
    cv2.destroyAllWindows()
