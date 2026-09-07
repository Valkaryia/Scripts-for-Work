from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
driver.get("www.xxxx.com")
#Put in the website that we need to pull reports in. left blanc for security reasons


UsNtxt = driver.find_element(by='id', value='UserName') #This finds the username
UsN = driver.find_element(by='id', value='UserName') 

Psdtxt = driver.find_element(by='id', value='Password') #This find the password
Psd = driver.find_element(by='id', value='Password')

Login = driver.find_element(by='id', value='btnLogin') #This find the login button
wait = WebDriverWait(driver, 30) #This creates the wait action for 30 seconds

wait.until
(
    EC.element_to_be_clickable((Login))
) #Makes the program wait until the login button is ready and available to click

UsN.click()
UsNtxt.send_keys("xxxxxxxxx")
Psd.click()
Psdtxt.send_keys("xxxxxxxxx")

Login.click()

driver.implicitly_wait(300)

Inv = driver.find_element(by='xpath', value='//a[@href="/Inventory/InventoryDetails"]') 
#Finds the xpath to the anchor element that we need, so we can visit the clickable link
#//ELEMENT_TYPE[@ATTRIBUTE="VALUE"] when trying to find elements on the page, the more specific you are the better. 
#* = any element or you can use 'div' or 'href' to find specific element that matches the attribute your looking for. 

wait.until
(
    EC.element_to_be_clickable((Inv))
) 
#Makes the program wait till Main page is loaded and buttons are clickable

Inv.click()

InvAF = driver.find_element(by='xpath', value='//a[@href="/Inventory/InventoryAllFields"]') 
#Finds the xpath to the anchor element that we need, so we can visit the clickable link

wait.until
(
    EC.element_to_be_clickable((InvAF))
) 
#Makes the program wait till Inventory page is loaded and buttons are clickable

InvAF.click()

Popup = driver.find_element(by='xpath', value='//div[@id="divPopUp"]') 
#Use the div element to find this specific class which is the entire popup window

#driver.execute_script("arguments[0].style.border='5px solid red';", Popup) 
#Use this to have selenium highlight the popup in red
wait.until
(
    EC.element_to_be_clickable(Popup)
)

ClosePopup = Popup.find_element(by='xpath', value='//div[@id="popFilter_HCB-1"]') 
#Div ID is mostly likely the interactable part of the HTML 
wait.until
(
    EC.element_to_be_clickable(ClosePopup)
)
ClosePopup.click()
#Once the popup appears this will close out of the filter.
#Revisit to use popup filter options instead of imbedded ones.

elements = driver.find_elements(by='xpath', value='//input[contains(@id,"DXFREditor")]')
print("Found:", len(elements))
for e in elements:
    print(e.get_attribute("id"))
#Creates the element to find all editable column within the page and prints them in terminal.
#More of a debugging helper so we know that we are calling from the correct available list.


Filter= driver.find_element(by='xpath', value='//tr[@class="dxgvFilterRow_Office2003Olive"]')
#Selects the overarching element where are the filters reside in.

Facility2 = Filter.find_element(by='xpath', value='//input[@id="gvInventory_DXFREditorcol50_I"]')
#This establishes the filter for facility and searches through the Filter area to locate the correct column.
Facility2.click()
Facility2.send_keys('Center of Excellence')

AuditGrade = Filter.find_element(by='xpath', value='//input[@id="gvInventory_DXFREditorcol38_I"]')
#This establishes the filter for Audit Grade and searches through the Filter area to locate the correct column.
AuditGrade.click()
AuditGrade.send_keys('X')

CatType = Filter.find_element(by='xpath', value='//input[@id="gvInventory_DXFREditorcol127_I"]')
#This establishes the filter for Category Type and searches through the Filter area to locate the correct column.
CatType.click()
CatType.send_keys('Non Core')

CatBtn = CatType.find_element(by='xpath', value="//img[contains(@onclick, \"GVFilterRowMenu('gvInventory',127\")]")
#This establishes the filter button for Category Type and searches through the Filter area to locate the correct column.
#Start using " instead of ' since we are looking and using strings that already contain a '
#The \" means that we are marking what is a string inside another set of "". That way the xpath function and Python strings dont get confused. 
CatBtn.click()

CatBtnMenu = CatBtn.find_element(by='xpath', value="//span[text()=\"Doesn't contain\"]")
#This finds the filter text options underneath the CatBtn for the CatType
CatBtnMenu.click()


driver.implicitly_wait(300)
#Applies a 300 milisecond wait that way all the information can correctly load or be selected on the screen before applying the filters to the database.

Apply = Filter.find_element(by='xpath', value='//td[@class="dxgvCommandColumn_Office2003Olive dxgv dx-ac"]')
Apply.click()

Csv = driver.find_element(by='xpath', value="//input[contains(@onclick, \"SetPrintType('CSV')\")]")
#Establishes the element for the CSV Report Download

Pg2 = driver.find_element(by='xpath', value="//a[contains(@onclick, \"ASPx.GVPagerOnClick('gvInventory','PN1')\")]")
#This establishes the elements of the 2nd page when all of the data load up from the website so we can download what we need from out filtered options

wait.until
(
    EC.element_to_be_clickable(Pg2)
)
#Makes the data load first before we click CSV to download.

Csv.click()

input ("Press Enter to close Edge. . .")
driver.quit()