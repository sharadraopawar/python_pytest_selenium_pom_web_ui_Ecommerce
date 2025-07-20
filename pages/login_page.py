from selenium.webdriver.common.by import By


class LoginPage:
    # def __init__(self,driver): # We are defining locators and actions of the web pages which will be used in testing
    #     self.driver=driver
    #     self.username=(By.ID,"Email")
    #     self.password=(By.ID,"Password")
    #     self.login_button=(By.CSS_SELECTOR,".button-1")
    #
    # def login(self,user,pwd):
    #     self.driver.find_element(*self.username).clear().send_keys(user)
    #     self.driver.find_element(*self.password).clear().send_keys(pwd)
    #     self.driver.login_button(*self.login_button).click()

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "Email")
        self.password = (By.ID, "Password")
        self.login_button = (By.CSS_SELECTOR, ".button-1")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()