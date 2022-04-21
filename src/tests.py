import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
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


def test_edit_profile():
    pass


def test_post_create_delete():
    pass
