from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.ID, 'cab_rental_vertical').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div.k7XPeRkvFNID3Ac9nWFA:last-child').click()
