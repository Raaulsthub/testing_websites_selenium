from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# loading driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open YouTube in the browser
driver.get('https://www.youtube.com')

print("Webpage title: " + driver.title)

# print driver.page_source would print the entire page source code

# Find the search input element
search_input = driver.find_element(By.NAME, 'search_query')

# Enter the search term "Messi" and press Enter
search_input.send_keys('Messi')
search_input.send_keys(Keys.ENTER)

# Wait for the search results page to load
wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.presence_of_element_located((By.ID, 'contents')))

# Get the URL of the new page
new_page_url = driver.current_url
print("New page URL: " + new_page_url)

driver.get(new_page_url)

# Wait for the page to fully load
wait = WebDriverWait(driver, 10)  # Adjust the timeout value as needed
wait.until(EC.presence_of_element_located((By.ID, 'video-title')))

# Find the video title in the search results
video_title = driver.find_element(By.ID, 'video-title')
print(video_title.text)

# click on the video
video_title.click()

time.sleep(200)
driver.quit()




