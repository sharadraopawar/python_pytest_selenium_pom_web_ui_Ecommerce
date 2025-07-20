import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


