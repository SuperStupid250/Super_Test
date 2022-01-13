from selenium import webdriver
import time

url = 'http://localhost:63342/29inchtest/Super_Test/mybaidu.html?_ijt=utavi89dnog4t4njaoeihbp7f3'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
a = driver.find_elements_by_xpath('//div[@class="card-body"]/table//tr/td[1]')
b = driver.find_elements_by_xpath('//div[@class="card-body"]/table//tr/td[5]/span')
# b = driver.find_element_by_xpath('//div[@class="card-body"]/table//tr[2]/td[5]/span').get_attribute('class')
for i,j in zip(a,b):
    title = i.text
    list = j.get_attribute('class')
    print(title +'----' +list)