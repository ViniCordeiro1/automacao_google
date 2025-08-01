from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    return driver

def pesquisar_no_google(driver, termo):
    driver.get("https://www.google.com")

    try:
        
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Aceitar')]"))
        ).click()
    except:
        pass  

    campo_busca = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    campo_busca.clear()
    campo_busca.send_keys(termo)
    campo_busca.send_keys(Keys.RETURN)

def clicar_primeiro_resultado(driver):
    try:
        primeiro_resultado = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h3'))
        )
        primeiro_resultado.click()
    except TimeoutException:
        print("⛔ Tempo esgotado ao tentar localizar o primeiro resultado.")
    except Exception as e:
        print(f"⛔ Erro ao clicar no resultado: {e}")

def main():
    termo_busca = "Python Selenium tutorial"
    driver = iniciar_driver()

    try:
        pesquisar_no_google(driver, termo_busca)
        clicar_primeiro_resultado(driver)

        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "title"))
        )
        print("📄 Página acessada:", driver.title)

    except Exception as erro:
        print("❌ Ocorreu um erro:", erro)

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
