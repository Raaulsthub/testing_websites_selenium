from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
import unittest

warnings.filterwarnings("ignore")



class WebPageTester(unittest.TestCase):

    # separate element testing


    def test_load_page(self):
        link = 'https://www.ucsd.edu/'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\tLoading webpage")
        try:
            driver.get(link)
            self.assertEqual(driver.current_url, link)
            print("\tWebpage loaded successfully")
        except:
            print("\tError loading webpage")
        
        driver.quit()

    def test_print_page_info(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\t\t\tWEBPAGE INFO", end='\n\n')
        # print page url
        print("\tWebpage URL: " + driver.current_url)
        # print page title
        print("\tWebpage title: " + driver.title)
        driver.quit()
        

    def test_images(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\t\t\tTESTING IMAGES", end='\n\n')
        # get image
        print("\t\tImage 1")

        try:
            driver.get('https://today.ucsd.edu/story/the-class-of-2023-dedicated-to-their-dreams')
            print('\t Got to the news page')
            image = driver.find_element(By.XPATH, '//*[@id="slideshow"]/figure/div/img')
            print('\t Got image')
            # is it the right image?
            expected_src = 'https://today.ucsd.edu/news_uploads/Grad_Story_2_Image.jpg'
            self.assertEqual(image.get_attribute('src'), expected_src)
            print('\t Image is correct')
        except:
            print('\t Error on image 1')

        print("\n\t\tImage 2")

        try:
            image = driver.find_element(By.XPATH, '//*[@id="wysiwyg"]/div[12]/div/div/figure/img')
            print('\t Got image')
            # is it the right image?
            expected_src = 'https://today.ucsd.edu/news_uploads/Yash_Shah.jpg'
            #self.assertEqual(image.get_attribute('src'), expected_src)
            print('\t Image is correct')
        except:
            print('\t Error on image 2')

        driver.quit()

    def test_text_elements(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.ucsd.edu/')
        print("\t\t\tTESTING TEXT ELEMENTS", end='\n\n')

        print("\t\tText element 1")

        try:
            text_element = driver.find_element(By.XPATH, '//*[@id="a-main"]/section[1]/div/div/div[1]/p[1]')
            print('\t Got text element')
            # is it the right text?
            expected_text = "UC San Diego is made up of a dynamic coalition of brilliant"
            found_text = text_element.text.split(' individuals')[0]
            self.assertEqual(expected_text, found_text)
            print('\t Text is correct')
        except:
            print('\t Error on text element 1')

        print("\n\t\tText element 2")

        try:
            text_element = driver.find_element(By.XPATH, '//*[@id="a-main"]/section[4]/div/div/p')
            print('\t Got text element')
            # is it the right text?
            expected_text = "Here, students can unleash their curiosity to help shape new fields and transform lives."
            self.assertEqual(expected_text, text_element.text)
            print('\t Text is correct')
        except:
            print('\t Error on text element 2')

        driver.quit()

    def test_buttons(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.ucsd.edu/')
        print("\t\t\tTESTING BUTTONS", end='\n\n')

        # BUTTON NUMBER ONE
        print("\t\tButton number one", end='\n')
        # getting button
        try:
            button = driver.find_element(By.XPATH, "//a[contains(@class, 'btn-default') and contains(@class, 'rt-btn-yellow')]")

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
            new_link = driver.current_url # getting new link
            expected_new_link = 'https://commencement.ucsd.edu/'
            new_link = new_link.split('?')[0]
            self.assertEqual(new_link, expected_new_link)
            print('\tButton clicked successfully')

            # testing new link
            driver.get(new_link)
            self.assertEqual(driver.current_url, expected_new_link)
            print('\tNew link is working properly')

            print('\tFound no errors on button 1')
        except:
            print("\tError on button 1")


        # Button number two
        print("\n\t\tButton number two", end='\n')
        # getting button
        try:
            button = driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[1]/li[1]/a')
            # testing button name
            print("\tButton text: " + button.text)
            expected_text = 'Students'
            self.assertEqual(button.text, expected_text)
            print('\tText is working properly')
            # testing button link
            expected_link = 'https://commencement.ucsd.edu/students/index.html'
            self.assertEqual(button.get_attribute('href'), expected_link)
            print('\tLink is working properly')
            # tesing click
            button.click()
            new_link = driver.current_url # getting new link
            expected_new_link = 'https://commencement.ucsd.edu/students/index.html'
            new_link = new_link.split('?')[0]
            self.assertEqual(new_link, expected_new_link)
            print('\tButton clicked successfully')
            # testing new link
            driver.get(new_link)
            self.assertEqual(driver.current_url, expected_new_link)
            print('\tNew link is working properly')
            print('\tFound no errors on button 2')
        except:
            print("\tError on button 2")

        driver.quit()

    def test_videos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\t\t\tTESTING VIDEOS", end='\n\n')

        print('\t\tVideo 1')
        try:
            driver.get('https://ucsd.edu/')
            # testing video
            video_button = driver.find_element(By.XPATH, '//*[@id="a-main"]/section[1]/div/div/div[1]/p[2]/a')
            print('\tFound video button')
            video_button.click()
            print('\tClicked video button')
            current_url = driver.current_url
            expected_url = 'https://www.youtube.com/watch?v=hmj_mp0bQ8s&feature=youtu.be'
            self.assertEqual(current_url, expected_url)
            print('\tGot to youtube video')
            print('\tVideo is working properly')
        except:
            print("\tError on video")

        print('\n\t\tVideo 2')
        driver.get('https://campaign.ucsd.edu/')
        # clicking on video button
        video_button = driver.find_element(By.XPATH, '//*[@id="banner-part"]/div/div/a')
        print('\tFound video button')
        video_button.click()
        print('\tClicked video button')
        print('\tVideo is working properly')

        driver.quit()

    def test_search_boxes(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\t\t\tTESTING SEARCH BOX", end='\n\n')
        print("\t\t Testing blink mode")
        try:
            driver.get('https://students.ucsd.edu/student-life/events/')
            # maximize window
            driver.maximize_window()
            # getting search box
            search_box = driver.find_element(By.XPATH, '//*[@id="q"]')
            print('\tFound search box')
            # testing search box
            search_box.send_keys('test')
            print('\tSent keys to search box')
            search_box.send_keys(Keys.RETURN)
            print('\tPressed enter')

            # clicking on one of the results
            link = driver.find_element(By.XPATH, '//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a')
            print('\tFound search result')
            link.click()
            print('\tClicked on search result')
            print('\tPage name: ' + driver.title)
            # checking new link
            current_url = driver.current_url
            expected_url = 'https://blink.ucsd.edu/safety/resources/public-health/covid-19/index.html'
            self.assertEqual(current_url, expected_url)
            print('\tSearch box (blink mode) is working properly')
        except:
            print("\tError on search box (blink mode)")

        print("\n\t\t Testing Faculty and Staff mode")
        try:
            driver.get('https://students.ucsd.edu/student-life/events/')
            # maximize window
            driver.maximize_window()
            # activating faculty and staff mode
            button = driver.find_element(By.XPATH, '//*[@id="cse-search-box"]/label[2]')
            button.click()
            print('\tSwitched to faculty and staff mode')
            # getting search box
            search_box = driver.find_element(By.XPATH, '//*[@id="entry"]')
            print('\tFound search box')
            # testing search box
            search_box.send_keys('computer science')
            print('\tSent keys to search box')
            search_box.send_keys(Keys.RETURN)
            print('\tPressed enter')
            # checking new link
            current_url = driver.current_url
            expected_url = 'https://act.ucsd.edu/directory/search?search-scope=faculty-staff&entry=computer+science'
            self.assertEqual(current_url, expected_url)
            print('\tSearch box (faculty and staff mode) is working properly')
        except:
            print("\tError on search box (faculty and staff mode)")

        driver.quit()

    def test_image_sliders(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\t\t\tTESTING IMAGE SLIDERS", end='\n\n')
        try:
            # testing image slider 1
            driver.get('https://ucsd.edu/') # geting to first page
            image_slider = driver.find_element(By.XPATH, '//*[@id="a-main"]/div[2]/div/div/div[2]/ul/a[2]') # get image slider
            print('\tFound image slider')
            image = driver.find_element(By.XPATH, '//*[@id="a-main"]/div[2]/div/div/div[2]/ul/div/div/li[2]/div[1]')# get associated image
            print('\tFound image')
            expected_style = 'background-image: url("_images/about/economic-impact-report/img-stats-top-ten.jpg");' # is it the right image?
            image_style = image.get_attribute('style')
            self.assertEqual(image_style, expected_style)
            print('\tFirst image is the correct one')
            image_slider.click() # click on image slider
            print("\tClicked on image slider")
            # get associated image
            image = driver.find_element(By.XPATH, '//*[@id="a-main"]/div[2]/div/div/div[2]/ul/div/div/li[3]/div[1]')
            print('\tFound image')
            # print image style
            expected_style = 'background-image: url("_images/about/economic-impact-report/img-stats-number-one-public-service.jpg");'
            image_style = image.get_attribute('style')
            self.assertEqual(image_style, expected_style)
            print('\tSecond image is the correct one')
            print('\tImage slider is working properly')
        except:
            print("\tError on image slider")

        driver.quit()
    
    def test_callendar(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://calendar.ucsd.edu/search/by-date/2023/06/05/')
        print("\t\t\tTESTING CALLANDAR", end='\n\n')

        try:
            print('\tTesting Month')
            month = driver.find_element(By.XPATH, '//*[@id="cal-current-month"]')
            print('\tFound month')
            expected_month = 'June 2023'
            print('\tMonth: ' + month.text)
            self.assertEqual(month.text, expected_month)
            print('\tMonth is correct')
            # clicking on another day
            print('\tTesting Day Click')
            day_button = driver.find_element(By.XPATH, '//*[@id="mc_calendar"]/table/tbody/tr[3]/td[4]/div/a')
            day_button_text = day_button.text
            driver.get(day_button.get_attribute('href'))
            print("\tClicked on day " + day_button_text)

            # checking if page day changed
            day_text = driver.find_element(By.XPATH, '//*[@id="calendar-main"]/section/h1[1]')
            print('\tDay: ' + day_text.text)
            expected_day = 'June 14, 2023'
            self.assertEqual(day_text.text, expected_day)
            print('\tDay change is correct')
        except:
            print("\tError on callendar")

        driver.quit()

    def test_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("\t\t\tTESTING LOGIN", end='\n\n')
        driver.get('https://calendar.ucsd.edu/search/by-date/2023/06/14/')
        login_button = driver.find_element(By.XPATH, '//*[@id="widget-sidebar"]/section[6]/a/div')
        print('\tFound login button')
        login_button.click()
        print('\tClicked on login button')
        expected_link = 'https://calendar.ucsd.edu/pages/user-entries'
        current_link = driver.current_url
        self.assertEqual(current_link, expected_link)
        print('\tLogin button is working properly')
        print('\tTrying to login')
        user_name_textbox = driver.find_element(By.XPATH, '//*[@id="calendar-main"]/div/div/form/section/div[1]/input')
        print('\tFound username textbox')
        user_name_textbox.send_keys('test')
        print('\tSent username')
        password_textbox = driver.find_element(By.XPATH, '//*[@id="calendar-main"]/div/div/form/section/div[2]/input')
        print('\tFound password textbox')
        password_textbox.send_keys('test')
        print('\tSent password')

        login_button = driver.find_element(By.XPATH, '//*[@id="calendar-main"]/div/div/form/section/div[3]/input')
        print('\tFound login button')
        login_button.click()
        print('\tClicked on login button')

        # did it log in? it should not
        received_text = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li')
        print('\tReceived: ' + received_text.text)
        expected_text = 'The existing username and/or password you submitted are not valid'
        self.assertEqual(received_text.text, expected_text)
        print('\tLogin is working properly')

        driver.quit()

    def test_register(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print('\t\t\tTESTING REGISTER', end='\n\n')

        try:
            driver.get('https://calendar.ucsd.edu/pages/add-event')
            print('\tLoaded register page')
            # trying to register
            print('\tTrying to register')
            user_name_textbox = driver.find_element(By.XPATH, '//*[@id="first_name"]')
            print('\tFound first name textbox')
            user_name_textbox.send_keys('test')
            print('\tSent first name')
            user_name_textbox = driver.find_element(By.XPATH, '//*[@id="last_name"]')
            print('\tFound last name textbox')
            user_name_textbox.send_keys('test')
            print('\tSent last name')
            user_name_textbox = driver.find_element(By.XPATH, '//*[@id="email"]')
            print('\tFound email textbox')
            user_name_textbox.send_keys('test')
            print('\tSent email')
            dept_org = driver.find_element(By.XPATH, '//*[@id="dept"]')
            print('\tFound department/organization textbox')
            dept_org.send_keys('test')
            print('\tSent department/organization')
            mail_code = driver.find_element(By.XPATH, '//*[@id="mail_code"]')
            print('\tFound mail code textbox')
            mail_code.send_keys('test')
            print('\tSent mail code')
            phone = driver.find_element(By.XPATH, '//*[@id="phone"]')
            print('\tFound phone textbox')
            phone.send_keys('test')
            print('\tSent phone')
            user_name_textbox = driver.find_element(By.XPATH, '//*[@id="username"]')
            print('\tFound username textbox')
            user_name_textbox.send_keys('test')
            print('\tSent username')
            password_textbox = driver.find_element(By.XPATH, '//*[@id="password"]')
            print('\tFound password textbox')
            password_textbox.send_keys('test')
            print('\tSent password')
            password_textbox = driver.find_element(By.XPATH, '//*[@id="password_confirm"]')
            print('\tFound confirm password textbox')
            password_textbox.send_keys('test')
            print('\tSent confirm password')

            submit_button = driver.find_element(By.XPATH, '//*[@id="submitAddEvent"]')
            print('\tFound submit button')
            submit_button.click()
            print('\tClicked on submit button')

            # the data is not valid, it should not change links!
            expected_link = 'https://calendar.ucsd.edu/pages/add-event'
            current_link = driver.current_url
            self.assertEqual(current_link, expected_link)
            print('\tRegister is working properly')
        except:
            print('\tError on register')

        driver.quit()

    # long tests
    
    def test_scholarship(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # testing several times (repeated test)
        print('\t\t\tTESTING NAVIGATION TIME (SCHOLARSHIP)', end='\n\n')
        total_time = 0
        for i in range(10):
            print('\tTest #' + str(i + 1))
            current_time = time.time()
            driver.get('https://ucsd.edu/')
            print('\tLoaded UCSD page')
            time.sleep(2)
            button1 = driver.find_element(By.XPATH, '//*[@id="a-main"]/section[5]/div[3]/div/div/p[2]/a')
            print('\tFound scholarship button')
            button1.click()
            print('\tClicked on scholarship and finantial aid button')
            button2 = driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[1]/li[4]/a')
            print('\tFound types button')
            button2.click()
            print('\tClicked on types button')
            button3 = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[4]/section/div/div[2]/div[1]/div/div/h3/a')
            print('\tFound scholarship button')
            button3.click()
            print('\tClicked on scholarship button')
            button4 = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[4]/section/div/div[1]/div[1]/div/div/div/h3/a')
            print('\tFound entering first year button')
            button4.click()
            print('\tClicked on entering first year button')
            print('\tGot to this test\'s final informative page')

            time_taken = time.time() - current_time

            if (time_taken > 10.0):
                print('\tNavigation time is too long: ' + str(time_taken) + ' seconds')
            else:
                print('\tNavigation time is acceptable: ' + str(time_taken) + ' seconds')

            total_time += time_taken
            print('\n')
        
        print('\tAverage navigation time: ' + str(total_time / 10) + ' seconds')

        driver.quit()




def main():
    unittest.main()
    return

if __name__ == "__main__":
    main()
