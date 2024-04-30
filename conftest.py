import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def setUp():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(4)
    driver.close()