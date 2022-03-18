from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from .form_create_campaign import FormCreateCampaign


class CampaignHome:
    def __init__(self, driver):
        self.driver = driver
