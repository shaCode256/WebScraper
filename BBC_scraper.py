import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import glob
import time
import re

def get_links():
    url = "https://www.bbc.com/"
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    links = []
    class_names_list= ["top-list-item__link", "block-link__overlay-link", ]
    for class_name in class_names_list:
        elems = driver.find_elements(By.CLASS_NAME, class_name)
        for elem in elems:
            links.append(elem.get_attribute('href'))
    return links

def get_page(url):
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
            f.write(url)
        f.close()

def is_phrase_in(phrase, text):
    return re.search(r"\b{}\b".format(phrase), text, re.IGNORECASE) is not None

def search_words(words):
    new_file_name= 'res ' +words+' '+str(time.time())+'.txt'
    search_results = open(new_file_name, "a")
    for file in glob.glob(os.path.join(os.getcwd(),'*.txt')):
        file1 = open(file, "r", encoding= "utf8")
        readfile = file1.read()
    # read file content
    # checking condition for string found or not
        if is_phrase_in(words, readfile):
            file1.seek(0)
            last_line = file1.readlines()[-1]
            search_results.write(last_line+"\n")#print the article url
    # closing a file
        file1.close()
    print("new file_name " + search_results.name)
    search_results.close()

def delete_txt_files():
    for filename in os.listdir(os.getcwd()):
        for file in glob.glob(os.path.join(os.getcwd(), '*.txt')):
            os.remove(os.path.join(os.getcwd(), file))



delete_txt_files()
#for link in get_links():
#        get_page(link)
#3search_words("high")

