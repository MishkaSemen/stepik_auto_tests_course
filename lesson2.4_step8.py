import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()

    browser.get(link)
    button =browser.find_element(By.CSS_SELECTOR, ".btn")

    text = WebDriverWait(browser,12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answerfield = browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(20)
    browser.quit()


