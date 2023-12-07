from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage


class RyDePage:
    """ This Class Contains all the necessary elements and methods"""

    # Click on Airport Transfer
    airport_transfer = (By.CSS_SELECTOR, 'div.k7XPeRkvFNID3Ac9nWFA:last-child')

    # Select Trip Type
    trip_type = (By.CLASS_NAME, 'hfzOHV5fBK_dqCntgiIu')
    from_airport = (By.XPATH, "//option[@value='From Airport']/parent::div")
    to_airport = (By.XPATH, "//option[@value='To Airport']/parent::div")

    # Select Airport /Terminal
    source = (By.ID, 'source')
    source_city = (By.XPATH, "//div[@class='bBl_VAKwVp5o7UJPlCNX']/div/div[2]")
    destination = (By.ID, 'destination')
    destination_values = (
        By.XPATH, "//div[@class='bBl_VAKwVp5o7UJPlCNX']/descendant::div[@class='FFaEHboqrbliXexCJfUL']")
    destination_select = (
        By.XPATH, "//div[@class='plUHKtBkypdrgSIM6HRa']/div[@id='clickbox']/div[@class='bBl_VAKwVp5o7UJPlCNX']")
    destination_city = (By.XPATH,
                        "//body/div[@id='reactContentMount']/div/div/div[@class='Dxl0JzRSsr9_vrb_UIAw']/div[@class='g3gfPcSN_QsfNofYaGXC']/div[@class='ld301i23Zx8IXiuZmK4d']/div[@class='plUHKtBkypdrgSIM6HRa']/div[@id='clickbox']/div[@class='bBl_VAKwVp5o7UJPlCNX']/div[1]/div[1]")

    # Date & Time Picker
    date = (By.CSS_SELECTOR, 'div.MuiInputBase-root input')
    date_picker = (By.XPATH,
                   "//button[@class='MuiButtonBase-root MuiIconButton-root MuiPickersDay-day MuiPickersDay-current "
                   "MuiPickersDay-daySelected']")
    hour = (
        By.XPATH,
        "//span[@class='MuiTypography-root MuiPickersClockNumber-clockNumber MuiTypography-body1'][text()='3']")
    minute = (
        By.XPATH,
        "//span[@class='MuiTypography-root MuiPickersClockNumber-clockNumber MuiTypography-body1'][text()='30']")
    # Search Button
    submit = (By.XPATH, "//span[text()='OK']/ancestor::button")
    search = (By.CSS_SELECTOR, "div.sIT1HvKpAi1b9I2CBe6s")

    ########################################################METHODS########################################################

    def __init__(self, driver):
        self.driver = driver
        HomePage(driver)

    def select_airport_transfer(self):
        return self.driver.find_element(*RyDePage.airport_transfer)

    def click_on_trip(self):
        return self.driver.find_element(*RyDePage.trip_type)

    def select_trip_type(self, value):
        if value == "From":
            return self.driver.find_element(*RyDePage.from_airport)
        elif value == "To":
            return self.driver.find_element(*RyDePage.to_airport)

    def select_airport_and_terminal(self):
        return self.driver.find_element(*RyDePage.source)

    def destination_location(self):
        return self.driver.find_element(*RyDePage.destination)

    def values_destinations(self):
        return self.driver.find_elements(*RyDePage.destination_values)

    def select_destination_value(self):
        return

    def select_destination(self, value):
        wait = WebDriverWait(self.driver,10)
        self.destination_location().send_keys(value)
        for elem in self.values_destinations():
            if elem.text == value:
                return elem.find_element(By.XPATH, "parent::div")
#     def select_city(self):
#         return self.driver.find_element(*RyDePage.source_city)
#
#     def destination_field(self):
#         return self.driver.find_element(*RyDePage.destination)
#
#     def click_date_field(self):
#         return self.driver.find_element(*RyDePage.date)
#
#     def select_date(self):
#         return self.driver.find_element(*RyDePage.date_picker)
#
#     def select_hours(self):
#         return self.driver.find_element(*RyDePage.hours)
#
#     def select_minutes(self):
#         return self.driver.find_element(*RyDePage.minutes)
#
#     def click_submit(self):
#         return self.driver.find_element(*RyDePage.submit)
#
#     def search_btn(self):
#         return self.driver.find_element(*RyDePage.search)
#
#     def hour_elem(self):
#         return self.driver.find_element(*RyDePage.hour)
#
#     def minute_elem(self):
#         return self.driver.find_element(*RyDePage.minute)
#
#
# """
# @FindBy(className = "pAF8mVcO_ALJRUwBz1nw")
# WebElement trip
#
#
# public void selecttriptype("From"):
#     if value == "From":
#
#
# """
