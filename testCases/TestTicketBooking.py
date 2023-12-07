import time

from selenium.webdriver.support import expected_conditions

from pageObjects.ryDe_Page import RyDePage
from utilites.BaseClass import BaseClass


class TestTicketBooking(BaseClass):

    # def test_from_search_functionality(self):
    #     red_bus = RyDePage(self.driver)
    #
    #     red_bus.click_on_trip().click()
    #     red_bus.select_trip_type("From").click()
    #
    #     red_bus.destination_location().send_keys("Nanakramguda")
    #     red_bus.select_destination_value("Nanakramguda").click()
    #     time.sleep(2)
    #     # self.driver.save_screenshot("image.png")

    def test_from_work(self):
        red_bus = RyDePage(self.driver)
        red_bus.click_on_trip().click()
        red_bus.select_trip_type("From").click()
        red_bus.select_destination("Shirdi").click()
        red_bus.select_airport_and_terminal().send_keys("Hyd")
        time.sleep(4)
