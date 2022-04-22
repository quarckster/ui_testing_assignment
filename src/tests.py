import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="module")
def selenium():
    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login():
    pass


def test_logout():
    pass


def test_register(selenium):
    # Load the page for registration
    selenium.get("http://microblog:5000/auth/register")
    # Fill in the fields
    username_field = selenium.find_element_by_id("username")
    username_field.send_keys("new_user")
    email_field = selenium.find_element_by_id("email")
    email_field.send_keys("new_user@example.org")
    password_field = selenium.find_element_by_id("password")
    password_field.send_keys("some_password")
    repeat_password_field = selenium.find_element_by_id("password2")
    repeat_password_field.send_keys("some_password")
    # Submit the form
    submit = selenium.find_element_by_id("submit")
    submit.click()
    # Check for the success message
    alert = selenium.find_element_by_xpath(".//div[@role='alert']")
    assert alert.text == "Congratulations, you are now a registered user!"


def test_edit_profile():
    pass


def test_post_create_delete():
    pass


def test_search():
    pass


def test_messages():
    pass


def test_follow():
    pass


def test_explore():
    pass
