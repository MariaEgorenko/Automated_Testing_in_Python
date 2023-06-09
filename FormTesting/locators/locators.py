from selenium.webdriver.common.by import By
from random import randint


class Locators:
    first_name = (By.CSS_SELECTOR, '#firstName')
    last_name = (By.CSS_SELECTOR, '#lastName')
    email = (By.CSS_SELECTOR, '#userEmail')
    gender = (By.CSS_SELECTOR, f'label[for="gender-radio-{randint(1, 3)}"]')
    mobile = (By.CSS_SELECTOR, '#userNumber')
    date_of_birth = (By.CSS_SELECTOR, '#dateOfBirthInput')
    subjects = (By.CSS_SELECTOR, '#subjectsInput')
    hobbies = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1, 3)}"]')
    file = (By.CSS_SELECTOR, '#uploadPicture')
    current_address = (By.CSS_SELECTOR, '#currentAddress')
    submit = (By.CSS_SELECTOR, '#submit')

    result_table = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
