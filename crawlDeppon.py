import urllib.request
from bs4 import BeautifulSoup
# import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")


# response = urllib.request.urlopen('https://www.deppon.com/deptlist/')
# # time.sleep(10)
# html = response.read()
# soup = BeautifulSoup(html, 'lxml')
# print(soup)
# items = soup.select("div[class='listA listA_Z'] a")
# print(items)
# for item in items:
#     print(item.string)

driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="F:/chromedriver")
driver.get("https://www.deppon.com/deptlist/")
html = driver.page_source
print(html)
# driver.find_element_by_link_text(u"新闻").click()
