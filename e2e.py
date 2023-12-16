from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys

PATH = r'C:\Program Files\chromedriver.exe'
web_driver = webdriver.Chrome(service=Service(PATH))


def test_scores_service(app_url):
    web_driver.get(app_url)
    game_score = WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.ID, 'scores')))
    s = game_score.text
    if 0 <= int(s) <= 1000:
        return True
    else:
        return False


def main_function(app_url):
    website_test = test_scores_service(app_url)
    print(website_test)
    if website_test:
        return sys.exit("0")
    else:
        return sys.exit("-1")


main_function("http://localhost:8777")

