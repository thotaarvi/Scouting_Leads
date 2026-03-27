from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Pages.AddLeadPage import Addlead
from Pages.Login_Page import  LoginPage
from Pages.Base import BASE_URL, USERNAME, PASSWORD
import pygsheets

import os
import base64
from Pages.popup_handler import handle_popups
from Pages.scoutlead import  ScoutLead



def get_leads_data():
    creds_base64 = os.getenv("GOOGLE_CREDS")

    if not creds_base64:
        raise Exception("GOOGLE_CREDS environment variable not set")

    # Create JSON file dynamically
    file_path = "service_account.json"

    with open(file_path, "w") as f:
        f.write(base64.b64decode(creds_base64).decode("utf-8"))

    # Authorize
    gc = pygsheets.authorize(service_account_file=file_path)

    sh = gc.open("Leadaddsheet2")
    worksheet = sh.sheet1

    return worksheet.get_all_records()


def test_valid_login(setup):
    driver = setup
    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)
    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()
    handle_popups(driver)

    # Navigate
    leads = Addlead(driver)
    leads.click_leads()

    scout = ScoutLead(driver)

    # Fetch data
    data = get_leads_data()

    for row in data:

        leads.click_addleads_button()
        leads.click_single_button()

        leads.enter_firstname(row["firstname"])
        leads.enter_lastname(row["lastname"])
        leads.enter_companyname(row["company"])
        leads.enter_emailname(row["email"])
        leads.enter_websitename(row["website"])

        leads.click_addlead()


        WebDriverWait(driver, 20).until(
            ec.invisibility_of_element_located((By.XPATH, "//button[text()='Add Lead']")))


        #scout.wait_for_row(row["email"])


        #scout.click_scout(row["email"])


        #scout.wait_for_completion(row["email"])




