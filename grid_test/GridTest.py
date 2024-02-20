import time
import unittest
import concurrent.futures

from selenium import webdriver
from selenium.webdriver.common.by import By
from Logic.logic_page import LogicPage
from infra.browser_wrapper import BrowserWrapper


class GridTest(unittest.TestCase):
    HUB_URL = 'http://172.20.10.3:4444'

    def setUp(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'mac'

        self.fireFox_cap = webdriver.FirefoxOptions()
        self.fireFox_cap.capabilities['platformName'] = 'mac'

        self.safari_cap = webdriver.SafariOptions()
        self.safari_cap.capabilities['platformName'] = 'mac'

        self.cap_list = [self.chrome_cap, self.fireFox_cap, self.safari_cap]
        self.browser = BrowserWrapper()

    def test_run_grid_serial(self):
        for cap in self.cap_list:
            self.test_execute(cap)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_execute, self.cap_list)

    def test_execute(self, cap):
        #one of the drivers & the logic working in one driver each time
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        print("test run on: ", cap.capabilities)

        self.assertEqual(" ", self.logic.execute(), "Title doesn't match expected value")
        time.sleep(2)
        self.driver.quit()

    def test_run_grid_serial_click_on_english_language(self):
        for cap in self.cap_list:
            self.test_click_on_english_language(cap)

    def test_run_grid_parallel_click_on_english_language(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_click_on_english_language, self.cap_list)

    def test_click_on_english_language(self, cap):
        #one of the drivers & the logic working in one driver each time
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        self.english_button = self.logic.click_on_english_button()
        assert self.english_button.is_displayed(), "Button is not displayed"
        time.sleep(2)
        self.driver.quit()

    def test_run_grid_serial_click_on_calender_button(self):
        for cap in self.cap_list:
            self.test_click_on_calender_button(cap)

    def test_run_grid_parallel_click_on_calender_button(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_click_on_calender_button, self.cap_list)

    def test_click_on_calender_button(self, cap):
        # one of the drivers & the logic working in one driver each time
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        self.calender_button = self.logic.click_on_calender_button()
        assert self.calender_button.is_displayed(), "Button is not displayed"
        time.sleep(2)
        self.driver.quit()

    def test_run_grid_serial_click_on_calender_date_button(self):
        for cap in self.cap_list:
            self.test_click_on_calender_date_button(cap)

    def test_run_grid_parallel_click_on_calender_date_button(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_click_on_calender_date_button, self.cap_list)

    def test_click_on_calender_date_button(self, cap):
        # one of the drivers & the logic working in one driver each time
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        self.calender_date_button = self.logic.click_on_calender_date_button()
        assert self.calender_date_button.is_displayed(), "Button is not displayed"
        time.sleep(2)
        self.driver.quit()

    def test_run_grid_serial_click_on_barcode_button(self):
        for cap in self.cap_list:
            self.test_click_on_barcode_button(cap)

    def test_run_grid_parallel_click_on_barcode_button(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_click_on_barcode_button, self.cap_list)

    def test_click_on_barcode_button(self, cap):
        # one of the drivers & the logic working in one driver each time
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        self.barcode_button = self.logic.click_on_barcode_button()
        assert self.barcode_button.is_displayed(), "Button is not displayed"
        time.sleep(2)
        self.driver.quit()

    def test_run_grid_serial_click_on_top_goals_profile(self):
        for cap in self.cap_list:
            self.test_click_on_top_goals_profile(cap)

    def test_run_grid_parallel_click_on_top_goals_profile(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_click_on_top_goals_profile, self.cap_list)

    def test_click_on_top_goals_profile(self, cap):
        #one of the drivers & the logic working in one driver each time
        self.driver = self.browser.get_driver(cap)
        self.logic = LogicPage(self.browser.get_driver(cap))

        self.top_goals_profile_button = self.logic.click_on_top_goals_profile_button()
        assert self.top_goals_profile_button.is_displayed(), "Button is not displayed"
        time.sleep(2)
        self.driver.quit()
