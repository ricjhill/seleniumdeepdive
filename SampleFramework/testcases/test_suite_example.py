import unittest

from SampleFramework.pageobjects.homescreen import HomeScreen
from SampleFramework.webdriver import Driver
from SampleFramework.values import strings


class TestSuiteExample(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.verify_banner_is_present()
        home_screen.verify_homelink_is_present()
        home_screen.verify_links_are_present()
        home_screen.verify_page_div_is_displayed()
        home_screen.verify_search_is_present()
        home_screen.verify_top_menu_sport_link_is_present()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
