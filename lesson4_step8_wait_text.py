from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
url = 'http://suninjuly.github.io/explicit_wait2.html'
driver.get(url)


price_rate = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
book_btn = driver.find_element(By.ID, 'book').click()

x_elem = driver.find_element(By.ID, 'input_value')
x = x_elem.text
y = calc(x)

ans_input = driver.find_element(By.ID, 'answer')
ans_input.clear()
ans_input.send_keys(y)

submit_btn = driver.find_element(By.ID, 'solve')
submit_btn.click()





