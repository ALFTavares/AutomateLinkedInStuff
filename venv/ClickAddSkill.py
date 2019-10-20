from selenium import webdriver
import constants as const


class Add_Skill:
    driver = None


    def __init__(self, driver):
        self.driver = driver


    def move_to_skills(self):
        self.driver.get(const.CONNECTIONS)


    def get_people(self):
        xpath = '//div[contains(@class, "mn-connection-card")]'
        list_of_people = self.driver.find_elements_by_xpath(xpath)
        return list_of_people
