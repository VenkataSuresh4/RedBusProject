import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://www.redbus.in/"


@pytest.fixture()
def setup(request):
    options = Options()
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
