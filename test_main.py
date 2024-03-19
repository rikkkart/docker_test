import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    return browser

def test_gidr(driver):
    driver.get("https://kemp103.ru/zhidkosti-dlya-gidravlicheskikh-sistem/")
    title = driver.find_element(By.TAG_NAME, 'h1')
    assert title.text == "Жидкости для гидравлических систем"

def test_akb(driver):
    driver.get("https://kemp103.ru/akb/")
    title = driver.find_element(By.TAG_NAME, 'h1')
    assert title.text == "АКБ"