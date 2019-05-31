from selenium import webdriver


class Accept():
    driver = None


    def __init__(self, driver):
        self.driver = driver


    def login(self, username, password):
        username_box = self.driver.find_element_by_id("username")
        password_box = self.driver.find_element_by_id("password")

        username_box.send_keys(username)
        password_box.send_keys(password)

        self.driver.find_element_by_class_name('login__form_action_container').click()


    def move_to_mynetwork(self):
        self.driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

        xpath = '//button[contains(@data-control-name,"accept")]'
        list_of_people_to_accept = self.driver.find_elements_by_xpath(xpath)
        return list_of_people_to_accept


    def accept_people(self, list_of_people):
        for person in list_of_people_to_accept:
            self.driver.execute_script("arguments[0].click();", person)


    def has_more(self):
        xpath = '//button[contains(@data-control-name,"accept")]'
        x = self.driver.find_elements_by_xpath(xpath)

        return len(x) > 0
