from selenium import webdriver
from time import sleep
import urllib.request
from selenium.webdriver.common.keys import Keys
import requests
import bs4
from selenium.webdriver.common.by import By
import csv

def yelp():


	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless") 
	driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)'}


	with open('data_set_yard_house.csv', 'w', newline='',encoding="utf-8") as csvfile:
		row = csv.writer(csvfile)
	
		counter = 0
		for i in range(1000):
			try:
				url = driver.get(f'https://www.yelp.com/biz/yard-house-sacramento-2?start={counter}')
			except:
				break
			res = requests.get(driver.current_url, headers=headers)
			res.raise_for_status()
			soup = bs4.BeautifulSoup(res.text, 'html.parser')

			#scroll down to the reviews
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			ul = driver.find_elements_by_tag_name('ul')
			li = ul[12].find_elements_by_tag_name('li')

			
			Rating_1 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(1) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_1 = Rating_1.get_attribute('aria-label')
			Rating_1 = Rating_1.split(' ')	

			#Body_Text_1 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(1) > div > div:nth-child(4) > p > span')
			Date_1 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(1) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 2-----------------------
			Rating_2 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(2) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_2 = Rating_2.get_attribute('aria-label')
			Rating_2 = Rating_2.split(' ')	

			#Body_Text_2 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(8) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(2) > div > div.margin-b2__373c0__abANL.border-color--default__373c0__2oFDT > p > span')
			Date_2 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(2) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 3-----------------------
			Rating_3 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(3) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_3 = Rating_3.get_attribute('aria-label')
			Rating_3 = Rating_3.split(' ')	

			#Body_Text_3 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(3) > div > div:nth-child(4) > p > span')
			Date_3 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(3) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 4-----------------------
			Rating_4 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(4) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_4 = Rating_4.get_attribute('aria-label')
			Rating_4 = Rating_4.split(' ')	

			#Body_Text_4 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(4) > div > div:nth-child(4) > p > span')
			Date_4 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(4) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 5-----------------------
			Rating_5 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(5) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_5 = Rating_5.get_attribute('aria-label')
			Rating_5 = Rating_5.split(' ')	

			#Body_Text_5 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(5) > div > div.margin-b2__373c0__abANL.border-color--default__373c0__2oFDT > p > span')
			Date_5 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(5) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 6-----------------------
			Rating_6 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(6) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_6 = Rating_6.get_attribute('aria-label')
			Rating_6 = Rating_6.split(' ')	

			#Body_Text_6 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(6) > div > div:nth-child(4) > p')
			Date_6 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(6) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 7-----------------------
			Rating_7 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(7) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_7 = Rating_7.get_attribute('aria-label')
			Rating_7 = Rating_7.split(' ')	

			#Body_Text_7 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(7) > div > div.margin-b2__373c0__abANL.border-color--default__373c0__2oFDT > p > span')
			Date_7 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(7) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 8-----------------------
			Rating_8 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(8) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_8 = Rating_8.get_attribute('aria-label')
			Rating_8 = Rating_8.split(' ')	

			#Body_Text_8 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(8) > div > div:nth-child(4) > p > span')
			Date_8 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(8) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span.css-e81eai')
			#------------------------------------------------------

			#---------------REVIEW SECTION 9-----------------------
			Rating_9 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(9) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_9 = Rating_9.get_attribute('aria-label')
			Rating_9 = Rating_9.split(' ')	

			#Body_Text_9 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(9) > div > div:nth-child(4) > p > span')
			Date_9 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(9) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------

			#---------------REVIEW SECTION 10-----------------------
			Rating_10 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(10) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
			Rating_10 = Rating_10.get_attribute('aria-label')
			Rating_10 = Rating_10.split(' ')	

			#Body_Text_10 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(10) > div > div.margin-b2__373c0__abANL.border-color--default__373c0__2oFDT > p > span')
			Date_10 = driver.find_element_by_css_selector('#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(7) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(10) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-fill__373c0__17z0h.border-color--default__373c0__2oFDT > span')
			#------------------------------------------------------


			li_1 = li[0].find_element_by_tag_name('p').text
			if li_1 == "Elite '2021":
				li_1 = li[0].text
			li_2 = li[1].find_element_by_tag_name('p').text
			if li_2 == "Elite '2021":
				li_2 = li[1].text
			li_3 = li[2].find_element_by_tag_name('p').text
			if li_3 == "Elite '2021":
				li_3 = li[2].text
			li_4 = li[3].find_element_by_tag_name('p').text
			if li_4 == "Elite '2021":
				li_4 = li[3].text
			li_5 = li[4].find_element_by_tag_name('p').text
			if li_5 == "Elite '2021":
				li_5 = li[4].text
			li_6 = li[5].find_element_by_tag_name('p').text
			if li_6 == "Elite '2021":
				li_6 = li[5].text
			li_7 = li[6].find_element_by_tag_name('p').text
			if li_7 == "Elite '2021":
				li_7 = li[6].text
			li_8 = li[7].find_element_by_tag_name('p').text
			if li_8 == "Elite '2021":
				li_8 = li[7].text
			li_9 = li[8].find_element_by_tag_name('p').text
			if li_9 == "Elite '2021":
				li_9 = li[8].text
			li_10 = li[9].find_element_by_tag_name('p').text
			if li_10 == "Elite '2021":
				li_10 = li[9].text

			rows_to_write = [[Rating_1[0], li_1, Date_1.text],[Rating_2[0], li_2, Date_2.text],[Rating_3[0], li_3, Date_3.text],[Rating_4[0], li_4, Date_4.text],[Rating_5[0], li_5, Date_5.text],[Rating_6[0], li_6, Date_6.text],[Rating_7[0], li_7, Date_7.text],[Rating_8[0], li_8, Date_8.text],[Rating_9[0], li_9, Date_9.text],[Rating_10[0], li_10, Date_10.text]]

			row.writerows(rows_to_write)

		
			print(f'done with task {i+1}')

			counter+=10





	#for i in ul_xpath:
	#	print(i.get_attribute('aria-label'))
	#for i in range(10):
	#	i = i+1
	#	rating_1 = driver.find_element_by_css_selector(f'#wrap > div.main-content-wrap.main-content-wrap--full > yelp-react-root > div > div.margin-t3__373c0__1l90z.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div > div.margin-b6__373c0__2Azj6.border-color--default__373c0__2oFDT > div > div.arrange-unit__373c0__1piwO.arrange-unit-grid-column--8__373c0__2yTAx.padding-r2__373c0__28zpp.border-color--default__373c0__2oFDT > div:nth-child(8) > section:nth-child(2) > div.css-79elbk.border-color--default__373c0__2oFDT > div > ul > li:nth-child(1) > div > div.margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT > div > div:nth-child(1) > span > div')
	#	print(rating_1.get_attribute('aria-label'))
	#print('----------------------------------')
	#print(ul_xpath.get_attribute('aria-label'))

	driver.quit()



def tripadvisor(url):
	pass







yelp()