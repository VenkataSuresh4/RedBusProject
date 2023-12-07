import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def action(self):
        return ActionChains(self.driver)

    def wait_for_element(self):
        return WebDriverWait(self.driver,10)

    def waitForEntry(self):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.ID, "source")))

    def waitForTextInput(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, 'destination')))

    def waitForDestElement(self):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH,
             "//body/div[@id='reactContentMount']/div/div/div[@class='Dxl0JzRSsr9_vrb_UIAw']/div[@class='g3gfPcSN_QsfNofYaGXC']/div[@class='ld301i23Zx8IXiuZmK4d']/div[@class='plUHKtBkypdrgSIM6HRa']/div[@id='clickbox']/div[@class='bBl_VAKwVp5o7UJPlCNX']/div[1]/div[1]")))

    def waitForDate(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//span/p[text()='26']/ancestor::button")))

    def waitForTripType(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.IBlOF5FQKOvVHh8JJUM2")))
