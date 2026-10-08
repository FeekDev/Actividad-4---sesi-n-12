from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        print("1. Abriendo la página de login...")
        driver.get("https://www.saucedemo.com")
        time.sleep(2)

        print("2. Iniciando sesión...")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        print("3. Agregando Backpack al carrito...")
        backpack_add_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack_add_button.click()
        time.sleep(3)

        print("4. Abriendo el carrito...")
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_button.click()
        time.sleep(5)

        print("5. Validando producto en el carrito...")
        assert "Sauce Labs Backpack" in driver.page_source
        print("Prueba aprobada.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()