# Python program to scrape table from website

# import libraries selenium and time
import itertools
import time
from itertools import groupby
import json
from selenium import webdriver
from time import sleep
import os
# Create webdriver object
from selenium.webdriver.common.by import By
from selenium import webdriver

def initialize_driver():
    options = webdriver.ChromeOptions()
    from selenium.webdriver.chrome.options import Options
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1280,800")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument('--disable-blink-features=AutomationControlled')
    #Add Proxy
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    # first tab. Open google.com in the first tab
    driver.get('http://google.com')
    # second tab
    driver.execute_script("window.open('about:blank','secondtab');")
    # It is switching to second tab now
    driver.switch_to.window("secondtab")
    # In the second tab, it opens IIA
    driver.get("http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx")
    sleep(2)
    driver.refresh();
    # Make Python sleep for some time
    sleep(2)
    # Print rows and columns
    #print(rows)
    #print(cols)
    # Printing the table headers

#save table content to txt
#def save_to_txt(driver):
    # Obtain the number of rows in body
    rows = 1 + len(driver.find_elements(By.XPATH,
                                        "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr"))
    sleep(2)
    # Obtain the number of columns in table
    cols = len(driver.find_elements(By.XPATH,
                                    "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr[1]/td"))
    new_file_name= 'table res '+str(time.time())+'.txt'
    table_txt = open(new_file_name, "a", encoding="utf-8")
    for r in range(1, rows + 1):
        for p in range(1, cols + 1):
            # obtaining the text from each column of the table
            value = driver.find_elements(By.XPATH,
                "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr[" + str(
                    r) + "]/td[" + str(p) + "]")
            for val in value:
                table_txt.write(val.text+ "\n")
    print("new file: "+new_file_name)
    table_txt.close()
    return new_file_name



def table_txt_to_json(txt_file_name):
    names = ["חברת תעופה", "טיסה", "נוחת מ", "טרמינל", "זמן מתוכנן", "תאריך", "זמן עדכני", "סטאטוס", "כלום"]
    with open(txt_file_name, 'r', encoding="utf8") as f_in, open('formatted.json', 'w', encoding="utf8") as f_out:
        lines= f_in.read()
        rows = lines.split("\n\n")
        listOfRows= []
        for doc in rows:
            doc = doc.split('\n')
            listOfRows.append(doc)

        finalList= []
        for row in listOfRows:
            finalRow= {}
            i=0
            for word in row:
                desc= names[i]
                finalRow[desc]=word
                i+=1
            finalList.append(finalRow)

        f_out.write( json.dumps(finalList, indent=4, ensure_ascii=False))
        f_out.close()
    f_in.close()

table_txt_to_json("table res 1649256578.6753902.txt")
#table_txt_to_json("res high 1649245719.8226411.txt")
