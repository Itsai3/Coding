from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements import BasePageElement
from locators import AgencyClientLocators, AgencyEmploymentLocators, AgencyMainPageLocators
import time
import openpyxl as xl
import xlrd

class BoxUser(BasePageElement): #Username Box
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'agency_auth_username'
class BoxPassword(BasePageElement):
    locator = 'agency_auth_password'

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    fill_username = BoxUser()
    fill_password = BoxPassword()

        
    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*AgencyMainPageLocators.GO_BUTTON)
        element.click()
        

class ContentItems(BasePage):

    def click_menu_button(self):
        
        element = self.driver.find_element(*AgencyMainPageLocators.GO_MENU)
        element.click()

    def new_employment(self):
        employments = self.driver.find_element(*AgencyEmploymentLocators.PLACEHOLDER) #<--- It's having trouble finding it because it's not visibly on the screen. Try to find a way to refocus it
        employments.click()

        self.driver.find_element()

    def new_client(self):
# Have to write a write an if conditions as a way to confirm if client profile is temporary
        self.driver.find_element(*AgencyMainPageLocators.GO_CLIENT).click()
        ### First Client Page. Is designed check for duplicate based on DOB and SSN 
        self.driver.find_element(*AgencyClientLocators.CLIENT_LAST_NAME).send_keys("Tsai") #<- Fill this in
        self.driver.find_element(*AgencyClientLocators.CLIENT_FIRST_NAME).send_keys("Irwin")
        # self.driver.find_element(*AddClientLocators.CLIENT_DOB).send_keys("")
        # self.driver.find_element(*AddClientLocators.CLIENT_SSN.send_keys(""))

        ### Second Client Page. Actually will input a profile after submit
        # self.driver.find_element(*AddClientLocators.CLIENT_MIDDLE_NAME.send_keys(""))
        # self.driver.find_element_by_xpath("//select[@id='numReturnSelect']/option[@value='15000']").click()
        # self.driver.find_element(*AddClientLocators.CLIENT_ALIAS.send_keys(""))
        # self.driver.find_element(*AddClientLocators.CLIENT_DOB).send_keys("") #<-- Check if you put in DOB in page 1, it'll go to page 2
        # self.driver.find_element(*AddClientLocators.CLIENT_SSN.send_keys("")) 


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source