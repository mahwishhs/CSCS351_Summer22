from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#enter your moodle credetionals here so that login could be successful
username = "576854"
password = "wrng password"

print("Initializing our webdriver...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://tmoodle.fccollege.edu.pk/moodle/login/index.php")

#To login
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

#For logging in (XPATH)
driver.find_element(By.XPATH,'//*[@id="loginbtn"]').click()

Page_title = driver.title
sleep(4)
#print(Page_title)

if Page_title ==   'Forman Christian College (A Chartered University)':
    print("Login SUCCESSFUL!")
else:
    print("Login FAILED")

