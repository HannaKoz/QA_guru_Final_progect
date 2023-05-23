from selene import browser, have, command, be
from selene.support.shared import browser

from final_project import resource


class RegistrationPage:

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def select_gender(self, gender):
        my_gender = gender
        if my_gender is 'Male':
            browser.element('[name=gender][value=Male]+[for=gender-radio-1]').click()
        elif my_gender is 'Female':
            browser.element('[name=gender][value=Female]+[for=gender-radio-2]').click()
        else:
            browser.element('[name=gender][value=Other]+[for=gender-radio-3]').click()
        return self

    def choose_hobbies(self, hobby):
        if hobby is 'Sports':
            browser.all('[class*=custom-checkbox]').element_by(have.text('Sports')).perform(
                command.js.scroll_into_view).click()
        elif hobby is 'Reading':
            browser.all('[class*=custom-checkbox]').element_by(have.text('Reading')).perform(
                command.js.scroll_into_view).click()
        elif hobby is 'Music':
            browser.all('[class*=custom-checkbox]').element_by(have.text('Music')).perform(
                command.js.scroll_into_view).click()
        else:
            ValueError('No hobby like this. Check spelling')
        return self

    def fill_birthday(self, day=int, month=int, year=int):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()
        return self

    def fill_subjects(self, firstLetters, subjectName):
        # Commerce
        browser.element('#subjectsInput').type(f'{firstLetters}') \
            .element(f'//div[contains(text(),"{subjectName}")]').click()
        # browser.element('#subjectsInput').type(f'{key_letters}').element('//div[contains(text(),"Commerce")]').click()
        return self

    def upload_file(self, fileName):
        browser.element('#uploadPicture').send_keys(resource.path(fileName))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#react-select-3-input').type(' ')
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#react-select-4-input').type(' ')
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()
        return self

    def submit_form(self):
        browser.element('[id="submit"]').submit()
        return self

    def registered_user(self, user):
        browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks"))
        browser.all('//tbody/tr')[0].should(have.text(user.first_name + " " + user.last_name))
        browser.all('//tbody/tr')[1].should(have.text(user.email))
        browser.all('//tbody/tr')[2].should(have.text(user.gender))
        browser.element('//tbody/tr[4]/td[2]').should(have.text(user.phone_number))
        browser.element('//tbody/tr[5]/td[2]').should(have.text(f'{user.day} August,{user.year}'))
        browser.element('//tbody/tr[6]/td[2]').should(have.text(user.subject))
        browser.element('//tbody/tr[7]/td[2]').should(have.text(user.hobby))
        browser.element('//tbody/tr[9]/td[2]').should(have.text(user.address))
        browser.element('//tbody/tr[9]/td[2]').should(have.text(user.address)).perform(
            command.js.scroll_into_view)  # - для маленбкого расширения скроллинг
        browser.element('//tbody/tr[10]/td[2]').should(have.text(f'{user.state} {user.city}'))
        return self

    def close_table_new_user(self):
        browser.element('[id="closeLargeModal"]').click()
        return self

    def new_form_open_assert(self):
        browser.element('#firstName').should(be.blank)
        browser.element('#lastName').should(be.blank)
        browser.element('#userEmail').should(be.blank)
        browser.element('#userNumber').should(be.blank)
        return self
