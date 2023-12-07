import time

from selenium.webdriver import ActionChains

from pageObjects.ryDe_Page import RyDePage
from utilites.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys


class TestAirport(BaseClass):

    # Positive
    def test_from_airport_search_Vehicles(self):
        ride_page = RyDePage(self.driver)

        # Click on "Airport Transfer"
        ride_page.select_airport_transfer().click()

        ride_page.source_field().send_keys("Hyd")
        self.waitForSourceElement()
        ride_page.select_city().click()
        #
        # self.waitForTextInput()
        # ride_page.destination_field().send_keys("Hitech")
        # self.waitForDestElement()
        # ride_page.select_destination().click()
        # time.sleep(2)
        # # Date Picker
        ride_page.click_date_field().click()
        ride_page.select_date().click()
        action = ActionChains(self.driver)
        action.move_to_element(ride_page.hour_elem()).click().perform()
        action.move_to_element(ride_page.minute_elem()).click().perform()
        # ride_page.clock_elem().click()
        # # i
        ride_page.click_submit().click()
        # #
        # ride_page.search_btn().click()

    # def test_to_airport_search_vehicles(self):
    #     ride_page = RyDePage(self.driver)
    #
    #     ride_page.airportTransfer().click()
    #
    #     ride_page.click_trip().click()
    #
    #     ride_page.select_trip_type("From").click()
    #
    #     ride_page.source_field().send_keys("Hyd")
    #
    #     ride_page.select_city("From").click()
    #
    #     ride_page.destination_field().send_keys("Mum")
    #
    #     ride_page.select_destination("From").click()
    #     time.sleep(3)
