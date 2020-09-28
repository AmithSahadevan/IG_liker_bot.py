
# You need to paste down the xpath of the target user's first post to make this work.("target_xpath_here")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = input("Username: ")
password = input("Password: ")
target = input("Target's username: ")

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    element.send_keys(username)

    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    element2.send_keys(password)
    element2.send_keys(Keys.RETURN)

    notnow1 = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
    )
    notnow1.click()

    notnow2 = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    )
    notnow2.click()

    instasearch = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    )
    instasearch.send_keys(target)
    instasearch.send_keys(Keys.RETURN)

    searchresult = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
    )
    searchresult.click()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    target_xpath_here = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div")
    )
    target_xpath_here.click()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    time.sleep(5)

    liking1 = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]")
    )
    liking1.click()

    nextbutton1 = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")
    )
    nextbutton1.click()

    time.sleep(5)

    for i in range(2,1000):

        for j in range(1000):

            liking1 = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]")
            )
            liking1.click()

            nextbutton2 = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a" + str([i]))
            )
            nextbutton2.click()
            time.sleep(5)

finally:
    driver.quit()
