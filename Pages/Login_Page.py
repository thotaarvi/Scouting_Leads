from selenium.webdriver.common.by import By

class LoginPage:

    username = (By.XPATH, "//input[@placeholder='Email']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()





