from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.set_window_size(1920, 1080)
driver.get("https://XXXXXX.com")
#Change website for secuirty reasons

UsNtxt = driver.find_element(by= 'id', value='UserName')
UsN = driver.find_element(by='id', value='UserName')

Psdtxt = driver.find_element(by= 'id', value='Password')
Psd = driver.find_element(by= 'id', value='Password')

Login = driver.find_element(by='id', value='btnLogin')
wait = WebDriverWait(driver, 30)

wait.until(
    EC.element_to_be_clickable((Login))
)

UsN.click()
UsNtxt.send_keys("XXXXX")
Psd.click()
Psdtxt.send_keys("XXXX")

Login.click()

driver.implicitly_wait(30)

Reports = driver.find_element(by='xpath', value='//a[@href="/Report/Index?group=INVENTORY"]')
wait.until(
    EC.element_to_be_clickable((Reports))
)
Reports.click()

Prod = driver.find_element(by='xpath', value='//a[@href="/Report?group=PRODUCTION"]')
wait.until(
    EC.element_to_be_clickable((Prod))
)
Prod.click()

DetailSum = driver.find_element(by='xpath', value=' //*[@id="ReportID"]/option[10]')
wait.until(
    EC.element_to_be_clickable((DetailSum))
)
DetailSum.click()

StartDate = driver.find_element(by='xpath', value='//*[@id="StartDate_B-1"]')
wait.until(
    EC.element_to_be_clickable((StartDate))
)
StartDate.click()

Today = driver.find_element(by='xpath', value='//*[@id="StartDate_DDD_C_BT"]')
wait.until(
    EC.element_to_be_clickable((Today))
)
Today.click()

EndDate = driver.find_element(by='xpath', value='//*[@id="EndDate_B-1"]')
wait.until(
    EC.element_to_be_clickable((EndDate))
)
EndDate.click()

EndToday = driver.find_element(by='xpath', value='//*[@id="EndDate_DDD_C_BT"]')
wait.until(
    EC.element_to_be_clickable((EndToday))
)
EndToday.click()

Csv = driver.find_element(by='xpath', value='//input[contains(@onclick, \"SetPrintToNormal()\")]')
wait
Csv.click()

input ("Press Enter to close Edge. . .")
driver.quit()