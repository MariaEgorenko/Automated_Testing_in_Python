from selenium.webdriver import Keys
from generator.generator import GeneratorPerson
from pages.base import BasePage
from locators.locators import Locators
from os import getcwd

class Form(BasePage):


    @property
    def fill_fields_and_submit(self):
        person = GeneratorPerson
        path = str(getcwd()) + r'\FormTesting\data\picture.jpg'
        self.remove_footer()
        self.element_is_visible(Locators.first_name).send_keys(person.first_name)
        self.element_is_visible(Locators.last_name).send_keys(person.last_name)
        self.element_is_visible(Locators.email).send_keys(person.email)
        self.element_is_visible(Locators.gender).click()
        self.element_is_visible(Locators.mobile).send_keys(person.mobile)
        subjects = self.element_is_visible(Locators.subjects)
        for subject in person.subjects:
            subjects.send_keys(subject)
            subjects.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.hobbies).click()
        self.element_is_visible(Locators.file).send_keys(path)
        self.element_is_visible(Locators.current_address).send_keys(person.current_address)
        self.element_is_visible(Locators.submit).click()
        return person
    
    def form_result(self):
        result_list = self.elements_are_visible(Locators.result_table)
        result_text = [i.text for i in result_list]
        return result_text

print(getcwd())