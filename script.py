import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)


def portal_login(email, password):
    driver.get("https://buhos.uson.mx/web/apps/portalAlumnos/index.php/login")

    driver.find_element_by_xpath('//*[@id="ext-gen1016"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="ext-gen1022"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="button-1018-btnEl"]').click()


def go_to_grades():
    # 'Mis Materiales'
    driver.find_element_by_xpath('//*[@id="1433"]').click()

    # Give time for iframe to load
    time.sleep(3)
    iframe = driver.find_element_by_xpath('//*[@id="ext-gen1036"]')
    driver.switch_to.frame(iframe)

    # Calificaciones
    driver.find_element_by_xpath('//*[@class="thumb-wrap"]').click()
    wait.until(EC.title_contains("UniSon"))


def check_for_grade():
    print('CHECKING GRADE...')
    time.sleep(5)
    pass


def refresh_page_every(seconds, loops):
    for _ in range(loops):
        wait.until(EC.title_contains("UniSon"))
        go_to_grades()
        check_for_grade()
        print('REFRESHING')
        driver.refresh()
        time.sleep(seconds)


def main():
    portal_login(os.environ['GRADE_USER'], os.environ['GRADE_PASSWORD'])
    print("Successfully logged in!")
    refresh_page_every(10, 5)
    print('============== FINISHED ==============')


if __name__ == '__main__':
    main()
