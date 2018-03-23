from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

visitedLinks=set()
file=open('lms.csv','r')
reader=csv.reader(file,delimiter=',')
for row in reader:
    user=row[0]
    passw=row[1]

driver=wb.Chrome(r'''C:\Users\<usr_name>\Downloads\chromedriver.exe''')
driver.maximize_window()
page=driver.get("http://mydy.dypatil.edu/")
wait = WebDriverWait(driver, 15)
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("next").send_keys(Keys.ENTER)
driver.find_element_by_name("password").send_keys(passw)
driver.find_element_by_id("loginbtn").send_keys(Keys.ENTER)
original = driver.get



def forumButton():
    
    driver.find_element_by_xpath("//*[@value='Add a new discussion topic']").send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.ID ,"id_subject"))).send_keys('Why Django?')
    wait.until(EC.presence_of_element_located((By.ID ,"id_messageeditable"))).send_keys('cause Django is best')

    

def openurl():
    for i in range(len(driver.window_handles)-1):
        driver.switch_to_window(driver.window_handles[1])
        url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT ,"https://www")))
        url.click()
        time.sleep(0.2)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])


def tryurl():
    driver.switch_to_window(driver.window_handles[2])
    url = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT ,"://")))
    url.click()
    time.sleep(0.5)
    driver.close()
    driver.switch_to_window(driver.window_handles[1])
 
def openpage(te):
    time.sleep(1)
    try:
        links=wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,te)))
        for x in range(0,len(links)):
            if links[x].is_displayed():
                links[x].send_keys(Keys.CONTROL+Keys.ENTER)
                tryurl()
    except TimeoutException:
        print("Exception has been thrown ")
		
def readpercent():
	span=driver.find_element(By.XPATH, '//*[@id="inst50217"]/div[2]/a/div/span').click()
	anchors = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'pending')))
	for item in reversed(range(0, len(anchors))):
		if anchors[item].is_displayed():
			anchors[item].send_keys(Keys.CONTROL + Keys.ENTER)
			time.sleep(2)
        
  
    
def getAllLinks():
    search = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME ,"inner_activities")))
    return search

def closeTabs():
	handles = driver.window_handles
	for x in range(0, (len(handles) - 1)):
		if x == 0:
			continue
		driver.switch_to_window(driver.window_handles[x])
		driver.close()
	driver.switch_to_window(driver.window_handles[0])
		


def isinset(a):
    print(visitedLinks)
    print('\n')
    return (a in visitedLinks)
            
def readmaterial():
    driver.find_element_by_link_text('Reading material').click()
    search=getAllLinks()
    for item in search:
        output=str(item.text)
        text=''.join(output)
        newtext=text.splitlines()
        for te in newtext:
            flag=isinset(te)
            if flag==False:
                visitedLinks.add(te)
                openpage(te)

def launch():
    links=driver.find_elements_by_class_name('launchbutton')
    for x in range(0,len(links)):
        links[x+2].send_keys(Keys.CONTROL+Keys.ENTER)
        driver.switch_to_window(driver.window_handles[1])
        visitedLinks.clear()
        readpercent()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

launch()
