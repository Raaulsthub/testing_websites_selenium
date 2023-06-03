from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
import unittest


class WebPageTester(unittest.TestCase):

    def test_run_tests(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning) # Ignore DeprecationWarning
        print('\n\n\t\t\tTESTING WEBPAGE', end='\n\n')
        self.load_driver()
        print('\n')
        self.load_page('https://www.ucsd.edu/')
        print('\n')
        self.print_page_info()
        print('\n')
        self.buttons()
        self.driver.quit()

    def load_driver(self):
        print('\tLoading driver')
        try:
            self.driver =  webdriver.Chrome(ChromeDriverManager().install())
            print("\tDriver loaded successfully")
        except:
            print("\tError loading driver")

    def load_page(self, link):
        print("\tLoading webpage")
        try:
            self.link =  self.driver.get(link)
            print("\tWebpage loaded successfully")
        except:
            print("\tError loading webpage")

    def print_page_info(self):
        print("\t\t\tWEBPAGE INFO", end='\n\n')
        # print page url
        print("\tWebpage URL: " + self.driver.current_url)
        # print page title
        print("\tWebpage title: " + self.driver.title)
        return

    def buttons(self):
        print("\t\t\tTESTING BUTTONS", end='\n\n')

        # BUTTON NUMBER ONE
        print("\t\t\tButton number one", end='\n')
        # getting button
        try:
            button = self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-default') and contains(@class, 'rt-btn-yellow')]")

            # testing button name
            print("\tButton text: " + button.text)
            expected_text = 'LEARN MORE ABOUT COMMENCEMENT'
            self.assertEqual(button.text, expected_text)
            print('\tText is working properly')

            # testing button link
            expected_link = 'https://commencement.ucsd.edu/'
            self.assertEqual(button.get_attribute('href'), expected_link)
            print('\tLink is working properly')

            # tesing click
            button.click()
            new_link = self.driver.current_url # getting new link
            expected_new_link = 'https://commencement.ucsd.edu/'
            new_link = new_link.split('?')[0]
            self.assertEqual(new_link, expected_new_link)
            print('\tButton clicked successfully')

            print('\tFound no errors on button 1')
        except:
            print("\tError on button 1")


    

def main():
    # tester = WebPageTester()
    # tester.run_tests()
    unittest.main()
    return

if __name__ == "__main__":
    main()
