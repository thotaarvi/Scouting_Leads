from selenium.webdriver.common.by import By


class Addlead:

    leads = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[2]/a")
    addLeads_button = (By.XPATH, "//button[text()='Add Leads']")

    single_button=(By.XPATH, "//button[text()='Single']")

    firstname = (By.XPATH, "//input[@name='first_name']")
    lastname = (By.XPATH,"//input[@name='last_name']")
    companyname = (By.XPATH, "//input[@name='company']")
    emailname = (By.XPATH,"//input[@name='email']")
    websitename = (By.XPATH,"//input[@name='website']")
    addlead = (By.XPATH,"//button[text()='Add Lead']")


    def __init__(self, driver):
        self.driver = driver


    def click_leads(self):
        self.driver.find_element(*self.leads).click()
    def click_addleads_button(self):
        self.driver.find_element(*self.addLeads_button).click()
    def click_single_button(self):
        self.driver.find_element(*self.single_button).click()

    def enter_firstname(self,firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)
    def enter_companyname(self,companyname):
        self.driver.find_element(*self.companyname).send_keys(companyname)
    def enter_emailname(self,emailname):
        self.driver.find_element(*self.emailname).send_keys(emailname)
    def enter_websitename(self,websitename):
        self.driver.find_element(*self.websitename).send_keys(websitename)
    def click_addlead(self):
        self.driver.find_element(*self.addlead).click()


