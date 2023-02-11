
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.forexfactory.com/calendar')

dates = driver.find_elements(by=By.CLASS_NAME, value='calendar__cell.calendar__date.date')
timers = driver.find_elements(by=By.CLASS_NAME, value='calendar__cell.calendar__time.time')
currencies = driver.find_elements(by=By.CLASS_NAME, value='calendar__cell.calendar__currency.currency')
events = driver.find_elements(by=By.CLASS_NAME, value='calendar__event-title')

for date, time, currency, event in zip(dates, timers, currencies, events):
    dater = date.text.strip() if date else ''
    timer = time.text.strip()
    currenc = currency.text.strip()
    even = event.text.strip()

    print(dater, timer, currenc, even)

driver.quit()