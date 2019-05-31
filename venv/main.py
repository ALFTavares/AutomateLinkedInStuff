from selenium import webdriver
from ClickAccept import Accept


def open_browser():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver_win32\chromedriver.exe',
                                  options=options)
        driver.minimize_window()
        return driver
    except Exception as e:
        print(str(e))


def get_linkedin_page():
    driver.get('https://www.linkedin.com/login/')


def login(username, password):
    username_box = driver.find_element_by_id("username")
    password_box = driver.find_element_by_id("password")

    username_box.send_keys(username)
    password_box.send_keys(password)

    driver.find_element_by_class_name('login__form_action_container').click()


def accept(accept_object):
    # keep refreshing the page, get the next 10 people in line and accept them
    while accept_object.has_more():
        people_to_accept = accept_object.move_to_mynetwork()
        accept_object.accept_people(people_to_accept)


def options_prompt():
    print('choose an option:')
    print('1: Accept Invites')
    return (input('option: '))


# add elif conditions to add more options
# you have to pass the driver as an argument. Don't forget
def choose_option(option, driver):
    if option == '1':
        accept_object = Accept(driver)
        accept(accept_object)
    else:
        print('Invalid option. Choose a valid one')
        choose_option(options_prompt(), driver)


if __name__ == '__main__':
    username = input('insert username\n')
    password = input('insert password\n')
    driver = None

    try:
        # open LinkedIn in login
        driver = open_browser()
        get_linkedin_page()
        login(username, password)

        choose_option(options_prompt(), driver)

        print('done successfully. ignore errors')
    except Exception as e:
        print('woops! something went wrong\nNow it\'s your chance to correct the problem :)')
        print(e)
    finally:
        if driver is not None:
            driver.quit()
        input('press any key to exit...')
