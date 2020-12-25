import time
import static

import file

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class Browser:
    def __init__(self):
        driver_Path = 'C:\Python39\chromedriver.exe'
        self.driver = webdriver.Chrome(driver_Path)
        self.driver.set_window_size(1000, 1000)
        Browser.openWebPage(self)

    def openWebPage(self):
        self.driver.get('https://ietts.gtb.gov.tr/Home/BelgeSorgula')
        try:
            w = WebDriverWait(self.driver, 10)
            w.until(expected_conditions.presence_of_element_located(
                (By.ID, 'IlId')))  # Check whether Drowpdown box of cities by xpath.
            print("Page load happened")
        except TimeoutException:
            print("Timeout happened no page load")
            self.driver.close()
        Browser.chooseCity(self)

    cityIndex = 17
    cityName = ''

    def chooseCity(self):
        self.cityIndex += 1
        for i in range(3, 82, 1):  # id=yok > ... , id=200 İç Ticaret
            self.driver.find_element_by_xpath('//option[@value="{}"]'.format(self.cityIndex)).click()
            self.cityName = self.driver.find_element_by_xpath('//option[@value="{}"]'.format(self.cityIndex)).text

            print(self.cityName)
            Browser.clickButton(self)
            time.sleep(2)

    def clickButton(self):
        goButtonClassName = 'btn btn-primary'
        try:
            w = WebDriverWait(self.driver, 5)
            w.until(expected_conditions.presence_of_element_located(
                (By.ID, 'btnSubmitDegisiklikFirmaAra')))  # Check whether Drowpdown box of cities by xpath.
            print("Button is active")
            button = self.driver.find_element_by_xpath(
                '//button[@class="{}"]'.format(goButtonClassName))  # goButton
            button.click()
            Browser.takeInformation(self)

        except TimeoutException:
            print("Timeout happened button isn't active")

    def takeInformation(self):
        try:
            w = WebDriverWait(self.driver, 5)
            w.until(expected_conditions.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="divResultTable"]/thead/tr/th[1]')))  # Check whether Drowpdown box of cities by xpath.
            print("Can take information")
        except TimeoutException:
            print("Can't take information")
        for c in range(1, 2, 1):
            city = 'Sehir'
            file.FileFunctions(city)
            for i in range(1, 7, 1):
                text = self.driver.find_element_by_xpath('//*[@id="divResultTable"]/thead/tr/th[{}]'.format(i)).text
                file.FileFunctions(text)
            rowCounter = 0

        for j in range(1, 10000000, 1):
            rowCounter += 1
            columnCounter = 0
            try:
                for j in range(1, 2, 1):
                    file.FileFunctions(self.cityName)
                    for i in range(1, 7, 1):
                        columnCounter += 1
                        text = self.driver.find_element_by_xpath(
                            '//*[@id="divResultTable"]/tbody/tr[{}]/td[{}]/span'.format(rowCounter, columnCounter)).text
                        file.FileFunctions(text)
                        # print('geri geldi mi')
            except:
                static.Foo.columnIndexDecrease(self)
                Browser.changePage(self)
                rowCounter = 1
                columnCounter = 1
                print('exception geldi breakten onmceeee')
                pass
                print('exception geldi bu son')

    def changePage(self):
        # self.driver.find_element_by_xpath('//li[@class="PagedList-skipToNext"]').find_element_by_tag_name('a').click()
        for i in range(1, 2, 1):
            try:
                element = self.driver.find_element_by_xpath(
                    '//li[@class="PagedList-skipToNext"]').find_element_by_tag_name(
                    'a')
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(2)
            except:
                print('passing to the oyelsine')

                Browser.chooseCity(self)
                break
