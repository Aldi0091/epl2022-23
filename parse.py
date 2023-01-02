import requests, lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support .ui import WebDriverWait

def browse():
    link = "https://olimpbet.kz/betting/index.php?page=line&action=2&sel[]=8100344"

    path = "/chromedriver/chromedriver"

    # chr_options = Options()
    # chr_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(path) #options=chr_options

    driver.get(link)

    script = "return document.querySelector('#i74680918').click()"

    # xpath = "//*[@id='r7571990_0'"
    
    # p = driver.find_element(By.XPATH, xpath)

    driver.execute_script(script)

    pageSource = driver.execute_script("return document.body.innerHTML;")

    with open("go.html", "a", encoding="utf-8") as file:
        file.write(pageSource)

    # with open("go.html", "r", encoding="utf-8") as file:
    #     source = file.read()
    # soup = BeautifulSoup(source, "html.parser")
    # block = soup.find("table","koeftable2").find_all("div", class_="tab")
    # for el in block:
    #     print(el)
if __name__ == "__main__":
    browse()
