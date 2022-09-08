from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as selenium_exceptions
PATH = 'H:\\chromedriver.exe'


def login():
    driver.find_element(By.ID, 'username').send_keys('206012')
    driver.find_element(By.ID, 'password').send_keys('redacted')


driver = webdriver.Chrome(PATH)
laip_url = 'https://courses.finki.ukim.mk/course/view.php?id=1696'
os_url = 'https://courses.finki.ukim.mk/course/view.php?id=1987'
# url = input('Enter the URL: ')
driver.get(os_url)
wait = ui.WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.ID, "page-course-view-topics")))
print(element)
i = 0
while True:
    el_id = f'section-{i}'
    try:
        ul = driver.find_element(By.ID, el_id)
    except selenium_exceptions.NoSuchElementException as e:
        break
    print(ul, el_id)
    i += 1

