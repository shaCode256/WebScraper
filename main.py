import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import glob

url = "https://www.bbc.com/"
options = webdriver.ChromeOptions()
options.headless = True

driver= webdriver.Chrome(options=options)

def get_links():
    driver.get(url)
    links = []
    class_names_list= ["top-list-item__link", "block-link__overlay-link", ]
    for class_name in class_names_list:
        elems = driver.find_elements(By.CLASS_NAME, class_name)
        for elem in elems:
            links.append(elem.get_attribute('href'))
    print(len(links))
    return links

def get_page(url):
    print("count")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='lxml')
    findings= soup.find('h1', {"id": "main-heading"})
    if findings:
        heading = findings.getText()
        with open( "".join(x for x in heading if x.isalnum())+'.txt', 'w', encoding="utf-8") as f:
            f.write(heading)
            f.write('\n')
            for block in soup.find_all('div', {"data-component": "text-block"}):
                if block:
                    f.write(block.getText())
                    f.write('\n')
            f.write("url: "+ url)
        f.close()

#for link in get_links():
#        get_page(link)

def search_words(words):
    for filename in os.listdir(os.getcwd()):
        for file in glob.glob(os.path.join(os.getcwd(),'*.txt')):
            file1 = open(file, "r")
            last_line = file1.readlines()[-1]
            print(last_line)
    # read file content
            readfile = file1.read()
    # checking condition for string found or not
            if words in readfile:
                print("hey")#print the article url
    # closing a file
            file1.close()


def delete_txt_files():
    for filename in os.listdir(os.getcwd()):
        for file in glob.glob(os.path.join(os.getcwd(), '*.txt')):
            os.remove(os.path.join(os.getcwd(), file))





#search_words("cost")
#delete_txt_files()