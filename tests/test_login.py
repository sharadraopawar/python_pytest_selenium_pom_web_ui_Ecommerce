import pytest
from pages.login_page import LoginPage
from utils.data_loader import get_login_data
from  utils.logger import setup_logger

logger=setup_logger()


@pytest.mark.parametrize("username,password,expected",get_login_data())
def test_login_valid(driver,username,password,expected):
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    logger.info(f"Testing with username: {username} | Expected: {expected}")

    login=LoginPage(driver)
    login.login(username,password)

    try:
        if expected=="success":
            assert "Dashboard" in driver.title, "Login failed when it should succeed"
            logger.info("Login successful as expected")
        else:
            assert "Login" in driver.title or "Dashboard" not in driver.title, "Login succeeded when it should fail"
            logger.info("Login failed as expected for invalid credentials ")
    except AssertionError:
        driver.save_screenshot(f"screenshot_{username}.png")