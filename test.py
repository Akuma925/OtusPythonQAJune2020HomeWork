from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from webdrivermanager import GeckoDriverManager

def test_elements():
    gdd = GeckoDriverManager()
    gdd.download_and_install()
    option = FirefoxOptions()
    b = webdriver.Firefox(options=option)
    b.get("https://otus.ru/")
    assert b.title == 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    b.close