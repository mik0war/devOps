import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5000"

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_calculator_operations(driver):
    # 1. Открываем страницу
    driver.get(BASE_URL)
    assert "Калькулятор" in driver.title

    # 2. Находим элементы
    num1 = driver.find_element(By.ID, "num1")
    num2 = driver.find_element(By.ID, "num2")
    result = driver.find_element(By.ID, "result")
    plus_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Сложить')]")

    # 3. Вводим числа и кликаем "+"
    num1.clear()
    num2.clear()
    num1.send_keys("5")
    num2.send_keys("3")
    plus_btn.click()

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element_value((By.ID, "result"), "8")
    )
    assert result.get_attribute("value") == "8"