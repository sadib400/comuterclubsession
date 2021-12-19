from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import find_connectable_ip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import pytz
options = Options()
options.headless = False
driver = webdriver.Chrome(options=options, executable_path=r'asdfg.exe')
i = 1
driver.get( "https://cutt.ly/7QedHym")
time.sleep(1)
fsdgfsd = driver.find_element_by_link_text("Log In").click()
fdggs = driver.find_element_by_id("m_login_email")
fdggs.send_keys("100070682388477")
dsffd = driver.find_element_by_name("pass")
dsffd.send_keys("asdewqt")
rrttt = driver.find_element_by_name("login")
rrttt.click()
while i <37:
    tz = pytz.timezone ("Asia/Dhaka")
    now = datetime.now(tz=tz)
    azxs = now.strftime("%I:%M %p")
    ghnj = now.strftime("%m/%d/%Y")
    try:
       active = driver.find_element_by_xpath("//span[@class='bk bl bm']")
    except:
        active = driver.find_element_by_css_selector("body > div.f:nth-child(1) > div#viewport > div#objects_container:nth-child(2) > div#root.e > div.bi:nth-child(1) > div:nth-child(1) > div.bj > span.bl.bm.bn:nth-child(2)")
    activetext = active.text
    print (active.text , end =" ")
    print("Current Time =", azxs, end =" ")
    driver.get("https://forms.gle/Es4mNXKtgZVuFwCh9")
    actv = driver.find_element_by_xpath("//input[@aria-describedby='i2 i3']")
    time.sleep(2)
    actv.click()
    time.sleep(1)
    actv.send_keys(activetext)
    wdfr = driver.find_element_by_xpath("//input[@aria-describedby='i6 i7']")
    time.sleep(2)
    wdfr.click()
    time.sleep(1)
    wdfr.send_keys(azxs)
    ctde = driver.find_element_by_xpath("//input[@aria-describedby='i10 i11']")
    time.sleep(2)
    ctde.click()
    time.sleep(1)
    ctde.send_keys(ghnj)
    subew = driver.find_element_by_xpath("//div[@jscontroller='VXdfxd']")
    subew.click() 
    print("respond" ,end =" ")
    print (i)
    i= i+1
    time.sleep(580)
    driver.get("https://cutt.ly/7QedHym")
    time.sleep(2)