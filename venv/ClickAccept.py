from selenium import webdriver


class Accept():
    driver = None


    def __init__(self, driver):
        self.driver = driver


    def move_to_mynetwork(self):
        self.driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')
        return get_people_to_accept()


    def get_people_to_accept(self):
        xpath = '//button[contains(@data-control-name,"accept")]'
        list_of_people_to_accept = self.driver.find_elements_by_xpath(xpath)
        return list_of_people_to_accept


    def accept_people(self, list_of_people_to_accept):
        for person in list_of_people_to_accept:
            self.driver.execute_script("arguments[0].click();", person)


    def has_more(self):
        xpath = '//button[contains(@data-control-name,"accept")]'
        x = self.driver.find_elements_by_xpath(xpath)

        return len(x) > 0
