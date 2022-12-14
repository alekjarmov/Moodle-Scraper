from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import yaml
from urllib.parse import urlparse
from urllib.parse import parse_qs
import os

with open('.\\config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

CHROMEDRIVER_PATH = config['chromedriver']

laip_url = 'https://courses.finki.ukim.mk/course/view.php?id=1696'
os_url = 'https://courses.finki.ukim.mk/course/view.php?id=1987'
courses_url = 'https://courses.finki.ukim.mk'
dna_url = 'https://courses.finki.ukim.mk/course/view.php?id=2051'
url = input('Enter the URL of the course: ')
file_to_save = input('Enter the file name where you want the recording links to be saved: ')
file_to_save = file_to_save.split('.')[0] + '.txt'


def login(driver: webdriver.Chrome):
    
    driver.get(url)
    my_login = config['Login']
    driver.find_element(By.ID, 'username').send_keys(my_login['username'])
    driver.find_element(By.ID, 'password').send_keys(my_login['password'])
    driver.find_element(By.CLASS_NAME, 'btn-submit').click()


def manual_login(driver: webdriver.Chrome):
    driver.get(url)
    wait = ui.WebDriverWait(driver, 60)
    element = wait.until(EC.presence_of_element_located((By.ID, "page-course-view-weeks")))


def cookie_login(driver: webdriver.Chrome):
    driver.get(courses_url)
    driver.delete_cookie('MoodleSession')
    driver.add_cookie(config['MoodleCookie'])
    driver.get(url)


login_type = {'auto': login, 'manual': manual_login, 'cookie': cookie_login}


def main() -> None:
    s = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=s)
    login_type[config['login_method']](driver)
    print('Logged in')
    bbb_img_url = 'https://courses.finki.ukim.mk/theme/image.php/classic/bigbluebuttonbn/1637059223/icon'
    images = driver.find_elements(By.CSS_SELECTOR, f'img[src="{bbb_img_url}"]')
    print(f'Found {len(images)} BBB images')
    num_images = len(images)
    # create a file with the links to the BBB sessions
    base_recording_url = 'https://bbb-lb.finki.ukim.mk/playback/presentation/2.3/'
    folder_name = 'recording_links'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(os.path.join(folder_name, file_to_save), 'w', encoding='utf-8') as f:
        for i in range(num_images):
            image = driver.find_elements(By.CSS_SELECTOR, f'img[src="{bbb_img_url}"]')[i]
            link = image.find_element(By.XPATH, '..')
            link.click()
            container_div = driver.find_element(By.ID, 'bigbluebuttonbn_recordings_table')
            if container_div.text == 'There are no recording to show.':
                print('No recordings found')
                driver.back()
                continue
            table = container_div.find_element(By.TAG_NAME, 'table')

            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows[1:]:
                try:
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    link = cells[0].find_element(By.TAG_NAME, 'a')
                    link_url = link.get_attribute('data-href')
                    name = cells[1].text
                    date = cells[5].text
                    # get the querystring rid of the link
                    parsed_url = urlparse(link_url)
                    rid = parse_qs(parsed_url.query)['rid'][0]
                    link_url = base_recording_url + rid
                    print(f'{name} {date} {link_url}')
                    f.write(f'{name} {date} {link_url}\n\n')
                except Exception as ex:
                    print(ex)
                    continue
            driver.back()

    driver.quit()


if __name__ == '__main__':
    main()
