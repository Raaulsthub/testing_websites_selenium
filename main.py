from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
import unittest

warnings.filterwarnings("ignore", category=DeprecationWarning) # Ignore DeprecationWarning

class WebPageTester(unittest.TestCase):
    #constructor 
    def __init__(self):
        super().__init__()

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
        # print page source
        # print(driver.page_source)
        return

    def test_buttons(self):
        print("\t\t\tTESTING BUTTONS", end='\n\n')

        # BUTTON NUMBER ONE
        print("\tButton number one", end='\n')
        # getting button
        try:
            button = self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-default') and contains(@class, 'rt-btn-yellow')]")
            # printing button text
            print("\tButton text: " + button.text)
            # testing button name
            expected_text = 'LEARN MORE ABOUT COMMENCEMENT'

        except:
            print("\tError getting button")

    
    def run_tests(self):
        print('\n\n\t\t\tTESTING WEBPAGE', end='\n\n')
        self.load_driver()
        print('\n')
        self.load_page('https://www.ucsd.edu/')
        print('\n')
        self.print_page_info()
        print('\n')
        self.test_buttons()
    

def main():
    tester = WebPageTester()
    tester.run_tests()
    

    return





if __name__ == "__main__":
    main()
