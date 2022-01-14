from selenium import webdriver
import requests, csv
import time
url = 'http://192.168.66.219/pan/nodes'
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('//*[@id="passwd"]').click()
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('Lock4Safe')
driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/form/button').click()

time.sleep(5)
f = open('C:/Users/Administrator/Desktop/123.csv', mode='a+', encoding='utf-8')
csv_writer = csv.writer(f)


a = driver.find_elements_by_xpath('//div[@class="card-body"]/table//tr/td[1]')
b = driver.find_elements_by_xpath('//div[@class="card-body"]/table//tr/td[5]/span')
# b = driver.find_element_by_xpath('//div[@class="card-body"]/table//tr[2]/td[5]/span').get_attribute('class')
for i,j in zip(a,b):
    title = i.text
    list = j.get_attribute('class')
    print(title +'----' +list)
    csv_writer.writerow([title,list])

f.close()





