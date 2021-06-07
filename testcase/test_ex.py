
import time

import pytest
from selenium import webdriver
def test_brower():
    driver = webdriver.Firefox(executable_path='/home/uk/PycharmProjects/browers/firefox/geckodriver')
    driver.get('https://www.amazon.in/')
    time.sleep(5)
    acttile  = driver.title
    extitle = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    time.sleep(5)
    assert acttile == extitle
    print('ending ')
    driver.close()
