from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.homelink = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, "Home")))
        self.topmenusport = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "orb-nav-sport")))
        self.banner = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "orb-banner")))
        self.links = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((
                By.TAG_NAME, "a")))
        self.page = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//*[@id='page']")))
        self.search = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "orb-search-form")))

    def verify_homelink_is_present(self):
        assert self.homelink.is_displayed()

    def verify_top_menu_sport_link_is_present(self):
        assert self.topmenusport.is_displayed()

    def verify_banner_is_present(self):
        assert self.banner.is_displayed()

    def verify_links_are_present(self):
        assert len(self.links) > 0

    def verify_page_div_is_displayed(self):
        assert self.twitter_button.is_displayed()
        assert self.linkedin_button.is_displayed()

    def verify_search_is_present(self):
        assert self.search.is_displayed()
