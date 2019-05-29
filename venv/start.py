from selenium import webdriver
from getpass import getpass
# TODO: getpass isn't working yet.. need to check why


def open_browser():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
        driver.minimize_window()
        driver.get('https://www.linkedin.com/login/')
        return driver
    except Exception as e:
        print(str(e))


def login(driver, username, password):
    username_box = driver.find_element_by_id("username")
    password_box = driver.find_element_by_id("password")

    username_box.send_keys(username)
    password_box.send_keys(password)

    driver.find_element_by_class_name('login__form_action_container').click()


def move_to_mynetwork(driver):
    driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

    xpath = '//button[contains(@data-control-name,"accept")]'
    list_of_people_to_accept = driver.find_elements_by_xpath(xpath)
    for person in list_of_people_to_accept:
        driver.execute_script("arguments[0].click();", person)


def has_more():
    xpath = '//button[contains(@data-control-name,"accept")]'
    x = driver.find_elements_by_xpath(xpath)

    return True if len(x) > 0 else False


username = input('insert username\n')
password = input('insert password\n')

try:
    driver = open_browser()
    login(driver, username, password)
    move_to_mynetwork(driver)

    while has_more():
        move_to_mynetwork(driver)

    print('done successfully. ignore errors')
except:
    print('woops! something went wrong\nNow it\'s your chance to correct the problem :)')
finally:
    driver.quit()
    input('press any key to exit...')

