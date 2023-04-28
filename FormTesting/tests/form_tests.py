from pages.form import Form

URL = 'https://demoqa.com/automation-practice-form'


class TestFormPage:

    def test_form(self, driver):
        form_page = Form(driver, URL)
        form_page.open()
        person = form_page.fill_fields_and_submit
        result = form_page.form_result()
        print(person, result, sep='\n')
        assert f'{person.first_name} {person.last_name}' == result[0], 'The form has not been filled'
        assert person.email == result[1], 'The form has not been filled'
