from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://moellim.riphah.edu.pk/login/index.php")
btn = driver.find_element("id", "username")
sleep(2)
btn.send_keys("fsd64147")
sleep(2)
driver.find_element("id", "password").send_keys("Insomnia12@moellim")
sleep(2)
driver.find_element("id", "rememberusername").click()
sleep(2)
driver.find_element("id", "loginbtn").click()
sleep(6)
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div[1]/section/div/aside/section/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[4]/div[1]/div/div[1]").click()
sleep(2)
driver.quit()