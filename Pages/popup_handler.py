def handle_popups(driver, timeout=5, max_attempts=5):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    for _ in range(max_attempts):
        try:
            wait = WebDriverWait(driver, timeout)

            btn = wait.until(
                ec.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(text(),'Close') or contains(text(),'Later') or contains(text(),'Got it') or contains(text(),'Skip')]"
                ))
            )
            btn.click()

        except:
            break  # no more popups → exit loop