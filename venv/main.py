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


if __name__ == '__main__':
    username = input('insert username\n')
    password = input('insert password\n')

    try:
        # open LinkedIn in login
        driver = open_browser()
        get_linkedin_page()

        # get Accept class
        accept = Accept(driver)

        # login
        accept.login(username, password)

        # keep refreshing the page, get the next 10 people in line and accept them
        while accept.has_more():
            people_to_accept = accept.move_to_mynetwork()
            accept.accept_people(people_to_accept)

        print('done successfully. ignore errors')
    except Exception as e:
        print('woops! something went wrong\nNow it\'s your chance to correct the problem :)')
        print(e)
    finally:
        driver.quit()
        input('press any key to exit...')

