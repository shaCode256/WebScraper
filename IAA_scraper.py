# Python program to scrape table from website

# import libraries selenium and time
import time

from selenium import webdriver
from time import sleep
import os
# Create webdriver object
from selenium.webdriver.common.by import By
from selenium import webdriver
# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # execute_script->Executes JavaScript snippet.
    # Here the snippet is window.open that means, it
    # opens in a new browser tab
    driver.execute_script("window.open('about:blank','secondtab');")
    # It is switching to second tab now
    driver.switch_to.window("secondtab")
    # In the second tab, it opens IIA
    # Get the website
    driver.get("http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx")
    sleep(2)
    driver.refresh();
    # Make Python sleep for some time
    sleep(2)
    # Obtain the number of rows in body
    rows = 1 + len(driver.find_elements(By.XPATH,
        "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr"))
    sleep(2)
    # Obtain the number of columns in table
    cols = len(driver.find_elements(By.XPATH,
        "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr[1]/td"))
    # Print rows and columns
    #print(rows)
    #print(cols)
    # Printing the table headers

#save table content to txt
def save_to_txt():
    new_file_name= 'table res '+str(time.time())+'.txt'
    table_txt = open(new_file_name, "a", encoding="utf-8")
    for r in range(1, rows + 1):
        for p in range(1, cols + 1):
            # obtaining the text from each column of the table
            value = driver.find_elements(By.XPATH,
                "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr[" + str(
                    r) + "]/td[" + str(p) + "]")
            descList= ["חברת תעופה", "טיסה", "נוחת מ", "טרמינל", "זמן מתוכנן", "זמן עדכני", "סטאטוס"]
            for val in value:
                table_txt.write(val.text+ "\n")
    print("new file: "+new_file_name)
    table_txt.close()

#save_to_txt()

def table_txt_to_json(txt_file_name):
    print("done")

