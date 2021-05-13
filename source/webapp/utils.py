import csv
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webapp.models import Company, Data


def get_data(url, company, driver):
    try:
        driver.get(url)
        print('search company')
        driver.find_element_by_id('yfin-usr-qry').send_keys(f'{company}')
        driver.find_element_by_id('header-desktop-search-button').click()
        link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-test='HISTORICAL_DATA']"))
        )
        link.find_element_by_css_selector("a").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "dateRangeBtn"))).click()
        driver.find_element_by_xpath("//button[@data-value='MAX']").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@download]"))).click()
        print('download file')
        time.sleep(10)
        print('ready')
    except Exception as e:
        print(e)
        print('! ' * 20, company, 'not find')


def open_file(f):
    file = open(f)
    reader = csv.reader(file)
    filename = os.path.basename(f)
    name = os.path.splitext(filename)[0]
    print(name)
    company, create = Company.objects.get_or_create(name=name)
    for row in reader:
        if row[0] == 'Date':
            continue
        data, _ = Data.objects.get_or_create(
            company=company,
            date=row[0],
            open=row[1],
            high=row[2],
            low=row[3],
            close=row[4],
            adj_close=row[5],
            volume=row[6]
        )


def get_companies_data():
    companies = Company.objects.all()
    companies_dict = {}
    for company in companies:
        companies_dict[company.name] = company.data.count()
    return companies_dict


def get_files(file_dir):
    try:
        files = os.listdir(file_dir)
        return files
    except FileNotFoundError:
        print(f'No such file or directory: {file_dir}')
        return None
