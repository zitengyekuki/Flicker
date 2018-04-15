#coding: utf-8
#!/usr/bin/python

import unittest
import time
from selenium import webdriver
import csv


class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def testEle(self):
        driver = self.driver
        driver.maximize_window()
        url = 'url'
        get_info(self, url)

    def tearDown(self):
        print 'down'


def get_info(self, url):
    driver = self.driver
    driver.get(url)
    time.sleep(5)
    views = driver.find_element_by_class_name('view-count-label').text
    fave = driver.find_element_by_class_name('fave-count-label').text
    comment = driver.find_element_by_class_name('comment-count-label').text
    aperture = driver.find_element_by_class_name('c-charm-item-aperture').find_element_by_tag_name('span').text
    focal_length = driver.find_element_by_class_name('c-charm-item-focal-length').find_element_by_tag_name(
        'span').text
    exposure_time = driver.find_element_by_class_name('c-charm-item-exposure-time').find_element_by_tag_name(
        'span').text
    iso = driver.find_element_by_class_name('c-charm-item-iso').find_element_by_tag_name('span').text

    with open("result.csv", "a+") as result_csvfile:
        writer = csv.writer(result_csvfile)
        row = [url, views, fave, comment, aperture, focal_length, exposure_time, iso]
        writer.writerow([unicode(s).encode("utf-8") for s in row])

    if driver.find_element_by_class_name('navigate-next'):
        next_page = driver.find_element_by_class_name('navigate-next')
        url = next_page.get_attribute('href')
        print url
        get_info(self, url)

if __name__ == "__main__":
    unittest.main()