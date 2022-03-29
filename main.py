import read_market
import mysql
from datetime import datetime
import time
import pyautogui
import random

def scan_pages(how_many_page):
    for _ in range(0,how_many_page):
        x = read_market.read_market()
        cnx = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='lost_ark_market_eu_central')
        for i in x:
            try:
                y = i[0]
                if y == "" or y == " ":
                    pass
                else:
                    cursor = cnx.cursor(buffered=True)
                    cursor.execute(""" SELECT item_id from item where name = "%s" """ % (i[0]))
                    selected_item = cursor.fetchall()
                    cursor.execute("""INSERT INTO details (avg_price, recent_price, lowest_price, cheapest_rem, item_id) 
                                VALUES (0, 0, %s, 0, %s)""" % (i[1], selected_item[0][0]))
                                
                    cnx.commit()
                    print("dodalem")
            except:
                print("nie dodalem")
                pass
        time.sleep(2)
        cords = pyautogui.locateOnScreen('next.png',confidence = 0.7)
        pyautogui.moveTo(cords)
        time.sleep(random.uniform(0.5,1))
        pyautogui.click()
        cnx.close()
        print("kolejna strona")
        time.sleep(random.uniform(0.5,1))

date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
while True:
    
    pyautogui.moveTo(random.randint(340,350),random.randint(468,478))
    pyautogui.click()
    time.sleep(random.uniform(0.5,1))
    scan_pages(4)
    time.sleep(2)
    pyautogui.moveTo(random.randint(340,350),random.randint(800,810))
    pyautogui.click()
    time.sleep(random.uniform(0.5,1))
    scan_pages(4)
    time.sleep(120)