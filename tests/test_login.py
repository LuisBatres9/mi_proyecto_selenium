#practica selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mensaje = driver.find_element(By.ID, "flash").text

    assert "You logged into a secure area!" in mensaje

    driver.quit()