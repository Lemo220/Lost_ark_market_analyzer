
import pytesseract
import cv2
from mss import mss
import mss.tools
import numpy as np
import mysql.connector

def read_market():
    y1 = 309
    y2 = 361
    y3 = 320
    y4 = 345

    all = []
    def take_screen(cords,number):
        with mss.mss() as sct:
                if number == True:
                    config = "--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.,"  ## config for number
                    fx = 4
                    fy = 4
                else:
                    config = """--oem 0 tessedit_char_whitelist=abcdefghijklmnoprstuwxyz[]"""  ## config for text
                    fx = 4
                    fy = 4
                x = sct.grab(cords)
                mss.tools.to_png(x.rgb, x.size, output='output.png')
                image = cv2.imread('output.png',cv2.IMREAD_GRAYSCALE)
                kernel = np.array([[0,-1,0],[-1, 5, -1],[0,-1,0]])
                im = cv2.filter2D(image, -1, kernel)
                if number == True: ## use this for image with number
                    
                    kernel = np.ones((2,2),np.uint8)
                    dilation = cv2.dilate(im,kernel,iterations = 1)
                    thresh = cv2.threshold(dilation,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                    double = cv2.resize(thresh, None, fx=fx, fy=fy) 
                    text = pytesseract.image_to_string(double, config=config)
                    text = text.replace("\n","").replace("""[Sold in bundles of 10 units]""","").replace("""[Sold in bundles of 100 units]""","").replace("%","").replace(",","")
                else: ## use this for image with text
                    double = cv2.resize(im, None, fx=fx, fy=fy) 
                    text = pytesseract.image_to_string(double, config=config)
                    text = text.replace("\n","").replace("""[Sold in bundles of 10 units]""","").replace("Peuh", "Pouch").replace("Peuch", "Pouch").replace("""[Sold in bundles of 100 units]""","").replace("%","").replace(u"\u2018","'").replace("!","l").replace("0", "o").replace("e'","e")
                print(text)
                return text
    for _ in range (0,10):
        price = []
        nazwa =(605,y1,809,y2)
        avg_price = (970,y3,1042,y4)
        recent_price = (1140, y3, 1202, y4)
        lowest_price = (1305,y3, 1362,y4)
        cheapest = (1530,y3,1622,y4)
        price.append(take_screen(nazwa, False))
        price.append(take_screen(avg_price, True))
        price.append(take_screen(recent_price, True))
        price.append(take_screen(lowest_price, True))
        price.append(take_screen(cheapest, True))
        y1 += 57
        y2 += 57
        y3 += 57
        y4 += 57
        all.append(price)
    return all






