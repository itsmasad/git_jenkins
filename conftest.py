import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def setUp():
    driver = webdriver.Chrome()
    yield driver
    print(driver.title)
    time.sleep(4)
    driver.close()