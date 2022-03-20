import time
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

ua = UserAgent()

opts = Options()
opts.headless = True
opts.add_argument("user-agent="+ua.random)
#driver = webdriver.Chrome(options=opts)
browser = webdriver.Chrome(options=opts)

# while True:
browser.get("https://www.canakit.com/raspberry-pi-4-8gb.html")
html = browser.page_source
soup = bs4.BeautifulSoup(html,"html.parser")

#item_in_store = soup.find_all('tr',{'height':'50'})
item_in_store = soup.find_all('span')['Pre-Order']
print(item_in_store)

in_stock = []

for product in item_in_store:
    if("Add to Cart" in product.text):
        # in_stock.append(product.find_all('a',href=True))
        print(product.find_parent('a')['href'])

# base_url = "https://www.canakit.com/"
#
# for url in in_stock:
#     url = base_url + url
#     print(url)
#
# #time.sleep(8)
#
# print("RUN FINISHED")
browser.quit()