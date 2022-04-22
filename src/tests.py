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
    """Test login with correct credentials
    Steps:
        1. Go to login page "http://microblog:5000/auth/login"
        2. Fill in username and password
        3. Click submit
        4. Check if user is logged in
        5. Logout
        6. Check if user is logged out
    """
    pass


def test_register(selenium):
    """Test register with correct credentials
    Steps:
        1. Go to register page "http://microblog:5000/auth/register"
        2. Fill in username, email, password and confirm password
        3. Click submit
        4. Check if alert has expected text
    """
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
    """Test edit profile with correct credentials
    Steps:
        1. Go to edit profile page "http://microblog:5000/edit_profile"
        2. Update "About me" fields
        3. Click submit
        4. Check if alert has expected text
        5. Check if "About me" fields are updated
        6. Revert all changes
    """
    pass


def test_post_create_delete():
    """Test create and delete post
    Steps:
        1. Go to main page "http://microblog:5000/"
        2. Fill "Say something" field
        3. Click submit
        4. Check if the post is created
    """
    pass


def test_search():
    """Test search
    Steps:
         1. Go to main page "http://microblog:5000/"
         2. Fill "Search" field
         3. Send "Enter" key
         4. Check if search results are empty
    """
    pass


def test_messages():
    """Test messages
    Steps:
        1. Create a new user
        2. Login as the new user
        3. Go to main user page
        4. Click on "Send private message"
        5. Fill in "Message" field
        6. Click submit
        7. Check if alert has expected text
        8. Logout
        9. Login as the main user
        10. Go to messages
        11. Check if message from another user is available
    """
    pass


def test_follow():
    """Test follow
    Steps:
        1. Create a new user
        2. Login as the new user
        3. Go to main user page
        4. Click on "Follow"
        5. Check if alert has expected text
        6. Logout
        7. Login as the main user
        8. Go to main user page
        9. Check if followers count is equal to 1
    """
    pass


def test_explore():
    """Test explore
    Steps:
        1. Submit three posts
        2. Go to explore page "http://microblog:5000/explore"
        3. Check if posts are available
    """
    pass
