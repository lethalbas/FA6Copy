from unicodedata import name
from selenium import webdriver
import sys
import os
import clipboard

try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = sys._MEIPASS
except Exception:
    # couldn't get _MEIPASS
    base_path = os.path.abspath(".")
# input for the name of the icon
iconName = input("type font awesome name: ")
# generate font awesome url
faUrl = "https://fontawesome.com/icons/" + iconName.replace("fa-", "")
# instantiate chrome webdriver
driver = webdriver.Chrome(base_path + "/chromedriver.exe")
print("chromedriver: " + base_path + "/chromedriver.exe")
# chrome driver get generated font awesome url
driver.get(faUrl)
# try finding and clicking copy button
try:
    driver.find_element("xpath","//*[@id=\"icon-landing\"]/div/div[2]/div/div/div[2]/div[2]/button").click()
    print("success! glyph copied to clipboard")
    # gets icon from the clipboard
    icon = clipboard.paste()
    # copies the new string with the name of the icon and the icon to the clipboard
    clipboard.copy(icon + " " + iconName)
    print("success! glyph text formated and copied to clipboard")
except:
    # chrome driver couldn't find the copy button
    print("error! copy button element not present, this could be due to a wrongly typed name")
# close chrome driver
driver.close()