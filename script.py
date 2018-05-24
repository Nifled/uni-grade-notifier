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

    driver.find_element_by_id("ext-gen1016").send_keys(email)
    driver.find_element_by_id("ext-gen1022").send_keys(password)
    driver.find_element_by_id("button-1018-btnEl").click()


def go_to_grades():
    # 'Mis Materiales'
    driver.find_element_by_id("1433").click()
    grade_link_id = "ext-gen1042"
    wait.until(EC.presence_of_element_located((By.ID, grade_link_id)))

    time.sleep(5)
    grade_link = driver.find_element_by_id("ext-gen1042")
    hover = action.move_to_element(grade_link)
    print("HOVER")
    hover.perform()
    time.sleep(5)

    # 'Calificaciones'


    # grade_link.click()
    # driver.find_element_by_id("ext-gen1041").click()
    wait.until(EC.title_contains("UniSon"))


def check_for_grade():

    pass


def refresh_page_every(seconds, loops):
    for _ in range(loops):
        wait.until(EC.title_contains("UniSon"))
        go_to_grades()
        print('REFRESHED')
        time.sleep(seconds)
        driver.refresh()


def main():
    portal_login(email, password)
    print("Successfully logged in!")
    refresh_page_every(10, 5)
    print('============== FINISHED ==============')


if __name__ == '__main__':
    main()
