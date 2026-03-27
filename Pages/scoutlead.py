from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ScoutLead:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 180)

    def wait_for_row(self, email):
        return self.wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, f"//table//tr[.//td[contains(normalize-space(),'{email}')]]")
            )
        )

    def click_scout(self, email):
        for _ in range(3):
            try:
                scout_btn = self.wait.until(
                    ec.element_to_be_clickable(
                        (By.XPATH, f"//tr[.//td[contains(normalize-space(),'{email}')]]//button[contains(.,'Scout')]")
                    )
                )

                self.driver.execute_script("arguments[0].click();", scout_btn)
                return

            except Exception:
                import time
                time.sleep(2)

        raise Exception(f"Scout button not clickable for {email}")

    def wait_for_completion(self, email):
        self.wait.until(
            lambda d: "Scouted" in d.find_element(
                By.XPATH,
                f"//tr[.//td[contains(normalize-space(),'{email}')]]"
            ).text
        )