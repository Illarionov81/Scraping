import os

from celery import shared_task
from selenium import webdriver

from webapp.utils import get_data, open_file

DIR = './downloads'
URL = 'https://finance.yahoo.com/'
COMPANIES = ['PD', 'ZUO', 'PINS', 'ZM', 'PVTL', 'DOCU', 'CLDR', 'RUN']


@shared_task
def get_company_data():
    save_dir = os.path.abspath('downloads')
    try:
        os.mkdir(save_dir)
        print('create dir')
    except OSError:
        print('dir already has ')
        pass
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/90.0.4430.93 Safari/537.36')
    prefs = {'download.default_directory': f'{save_dir}'}
    options.add_experimental_option('prefs', prefs)
    path_to_driver = os.path.abspath('chromedriver')
    driver = webdriver.Chrome(executable_path=path_to_driver, options=options)

    for company in COMPANIES:
        print('#' * 30)
        print(company)
        print('#' * 30)
        get_data(URL, company, driver)
    driver.close()
    driver.quit()


@shared_task
def parse_all_files():
    try:
        print('Start parsing . . . ')
        files = os.listdir(path=DIR)
        for f in files:
            file = os.path.relpath(f)
            open_file(os.path.join(DIR, file))
    except FileNotFoundError:
        print(f'No such file or directory: {DIR}')
