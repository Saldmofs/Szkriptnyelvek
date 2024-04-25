#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    browser = webdriver.Firefox()
    browser.get('https://clickcounter.io/')
    up = browser.find_element(By.XPATH, '//*[@id="up"]')
    
    i = 0
    
    while i < 2023:
        up.click()
        i += 1

    browser.save_screenshot("2023.png")

if __name__ == '__main__':
    main()
