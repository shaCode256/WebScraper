# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from time import sleep

# Create webdriver object
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()

# Get the website
driver.get(
    "https://www.iaa.gov.il/airports/ben-gurion/flight-board")

# Make Python sleep for some time
sleep(2)

# Obtain the number of rows in body
rows = 1 + len(driver.find_elements(By.XPATH,
    "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr"))

# Obtain the number of columns in table
cols = len(driver.find_elements(By.XPATH,
    "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr[1]/td"))

# Print rows and columns
print(rows)
print(cols)

# Printing the table headers
print("Locators		 " + "			 Description")

# Printing the data of the table
for r in range(2, rows + 1):
    for p in range(1, cols + 1):
        # obtaining the text from each column of the table
        value = driver.find_elements(By.XPATH,
            "/html/body/div[2]/main/article/section/div[3]/div[1]/div/div/table/tbody/tr[" + str(
                r) + "]/td[" + str(p) + "]")
        for val in value:
            print(val.text)
    print()

