from final_project.Pages import RegistrationPage
from final_project.data.data import user_male


def test_form(browser_size_w1280_h720):
    user = user_male
    (
        RegistrationPage()

        .fill_first_name(user.first_name)
        .fill_last_name(user.last_name)
        .select_gender(user.gender)

        .fill_email(user.email)
        .fill_phone_number(user.phone_number)

        .fill_birthday(user.day, user.month, user.year)
        .fill_subjects(firstLetters=user.key_letters, subjectName=user.subject)
        .choose_hobbies(user.hobby)
        .upload_file(user.file_name)

        # Fill address
        .fill_address(user.address)
        .select_state(user.state)
        .select_city(user.city)

        .submit_form()

        # Assert registered user result data
        .registered_user(user_male)
        .close_table_new_user()

        # Assert page after registration finished
        .new_form_open_assert()
    )
