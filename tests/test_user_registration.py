from selene.support.shared import browser

from demo_qa_tests.model.pages import registration_form
from utils import unit_9_attach



def test_submit_student_details(open_and_quit_browser_automation_practice_form):
    registration_form.set_first_name('Никита')
    registration_form.set_last_name('Кузнецов')
    registration_form.set_email('mamintargetolog@gmail.com')
    registration_form.set_gender('Male')
    registration_form.set_phone_number('9111111111')
    registration_form.set_date_of_birth([19, 'November', '1991'])
    registration_form.set_subject('English')
    registration_form.set_hobby('Music')
    registration_form.set_picture('resources/picture.jpg')
    registration_form.set_address('Russia, Moscow')

    registration_form.scroll_to_bottom()
    registration_form.set_state('Haryana')
    registration_form.set_city('Karnal')

    registration_form.click_submit()

    registration_form.should_have_submitted(
            [
                ('Student Name', 'Никита Кузнецов'),
                ('Student Email', 'mamintargetolog@gmail.com'),
                ('Gender', 'Male'),
                ('Mobile', '9111111111'),
                ('Date of Birth', '19 November,1991'),
                ('Subjects', 'English'),
                ('Hobbies', 'Music'),
                ('Picture', 'picture.jpg'),
                ('Address', 'Russia, Moscow'),
                ('State and City', 'Haryana Karnal')
            ],
        )
    unit_9_attach.add_logs(browser)
    unit_9_attach.add_screenshot(browser)
    unit_9_attach.add_html(browser)



