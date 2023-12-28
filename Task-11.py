# Using Python Selenium Automation and Action Chains visit the URL https://jquervui.com/droppable/
# and do a Drag and Drop operation of the White Rectangular Box into the Yellow Rectangular Box?

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.get("https://jqueryui.com/droppable/")

# To move to frame
frame_1 = driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(frame_1)

# Drag - White Rectangular Box
drag_me = driver.find_element(By.ID,"draggable")
# Drop - Yellow Rectangular Box
drop_here = driver.find_element(By.ID,"droppable")

actions = ActionChains(driver)
actions.drag_and_drop(drag_me,drop_here).perform()
time.sleep(3)

driver.quit()