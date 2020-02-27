import re
import config
from robobrowser import RoboBrowser
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://academia.srmist.edu.in/")
driver.find_element_by_xpath("//*[@placeholder='Email Address']").send_keys("as4855@srmist.edu.in")
# driver.find_element_by_xpath("//*[@id='signinForm']/div[5]/input").click()
# //*[@id='Email']//*[@id="Email"]
# //*[@id="Password"]
driver.implicitly_wait(4)
driver.find_element_by_xpath("//*[@placeholder='Password']").send_keys("Monu@1998")
driver.find_element_by_xpath("//*[@id='signinForm']/div[5]/input").click()