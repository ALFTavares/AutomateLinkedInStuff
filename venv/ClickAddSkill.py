from selenium import webdriver
import constants as const


class Add_Skill:
    driver = None


    def __init__(self, driver):
        self.driver = driver


    def move_to_skills(self):
        self.driver.get(const.CONNECTIONS)

