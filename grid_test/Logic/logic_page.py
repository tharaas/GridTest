from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class LogicPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def execute(self):
        return self.driver.title

    def english_button(self):
        self.ENGLISH_BUTTON = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/footer/div/div[5]/div/div/div[2]/div[2]")

    def click_on_english(self):
        self.ENGLISH_BUTTON.click()

    def click_on_english_button(self):
        self.english_button()
        self.click_on_english()
        return self.ENGLISH_BUTTON

    def calender_button(self):
        self.CALENDER_BUTTON = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[3]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div")

    def click_on_calender(self):
        self.CALENDER_BUTTON.click()

    def click_on_calender_button(self):
        self.calender_button()
        self.click_on_calender()
        return self.CALENDER_BUTTON

    def calender_date_button(self):
        self.CALENDER_DATE_BUTTON = self.driver.find_element(By.XPATH, "//*[@id='tippy-111']/div/div[1]/div/div/div/div/div/div/table/tbody/tr[5]/td[4]")

    def click_on_calender_date(self):
        self.CALENDER_DATE_BUTTON.click()

    def click_on_calender_date_button(self):
        self.calender_button()
        self.click_on_calender()
        self.calender_button()
        self.click_on_calender()
        return self.CALENDER_DATE_BUTTON

    def setting_button(self):
        self.SETTING_BUTTON = self.driver.find_element(By.CLASS_NAME, "main-header-module-settings-button")

    def click_on_setting(self):
        self.SETTING_BUTTON.click()

    def click_on_setting_button(self):
        self.setting_button()
        self.click_on_setting()

    def barcode_button(self):
        self.BARCODE_BUTTON = self.driver.find_element(By.XPATH, "//*[@id='tippy-432']/div/div/div/div/div/div[1]/div[4]/div[2]")

    def click_on_barcode(self):
        self.BARCODE_BUTTON.click()

    def click_on_barcode_button(self):
        self.barcode_button()
        self.click_on_barcode()
        return self.BARCODE_BUTTON

    def top_goals_profile_button(self):
        self.TOP_GOALS_BUTTON = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/a[1]")

    def click_on_top_goals_button(self):
        self.TOP_GOALS_BUTTON.click()

    def click_on_top_goals_profile_button(self):
        self.top_goals_profile_button()
        self.click_on_top_goals_button()
        return self.TOP_GOALS_BUTTON
