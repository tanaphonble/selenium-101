import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_current_date(self):
        return time.strftime('%d/%m/%Y')        

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, text))
        )

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
