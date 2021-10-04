from selenium.webdriver.common.by import By

###AGENCY
class AgencyMainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.NAME, 'logbutton')
    GO_MENU = (By.LINK_TEXT, 'Menu')
    GO_CLIENT = (By.LINK_TEXT, 'Add Client')

    

class AgencyEmploymentLocator(object):

    # Add a new employment record
    EMPLOYMENT_ADD = (By.LINK_TEXT, 'Add a new staff account')
    EMPLOY_USER = (By.NAME, "rec[username]")
    EMPLOY_STAFF = (By.NAME, "rec[staff_email]")
    EMPLOY_LAST_NAME = (By.NAME, "rec[name_last]")
    EMPLOY_FIRST_NAME = (By.NAME, "rec[name_first]")
    EMPLOY_LEGAL_NAME = ((By.NAME, "rec[name_first_legal]"))

class AgencyClientLocators(object):

    CLIENT_GO = (By.CLASS_NAME, "engineButton")
    CLIENT_TEMPORARY = ()
    CLIENT_LAST_NAME = (By.NAME, "rec[name_last]")
    CLIENT_FIRST_NAME = (By.NAME, "rec[name_first]")
    CLIENT_MIDDLE_NAME = (By.NAME, "rec[name_middle]")
    CLIENT_DOB = (By.NAME, "rec[dob]")
    CLIENT_SSN = (By.NAME, "rec[ssn]")
    CLIENT_ALIAS = (By.NAME, "rec[name_alias]")

class AgencyEmploymentLocators(object):

    PLACEHOLDER = "okay"

class ClarityMainPageLocators(object):

    LOGIN_USER = (By.ID, "username")
    LOGIN_PASS = (By.ID, "password")
    LOGIN_GO = (By.ID, "signin-button")
    GO_CLIENT = (By.XPATH, '//a[@href="/client/profile/add"]')
    SEARCH_MAIN = (By.LINK_TEXT, "Search")
    RESENT_GO = (By.ID, "btn-send-code")
    AGENCY_SWITCH_CARROT = (By.ID, "launchbar_agency")
    GO_CEA = (By.LINK_TEXT, "Coordinated Entry System Agency")
    SEARCH_CLIENT = (By.ID, "id-search")
    SEARCH_GO = (By.CLASS_NAME, "btn-search")

class ClarityNewClient(object):

    ADD_SSN = (By.ID, "ssn1")
    ADD_QSSN = (By.ID, "q_ssn")
    ADD_LAST_NAME = (By.ID, "last_name")
    ADD_FIRST_NAME = (By.ID, "first_name")
    ADD_MIDDLE_NAME = (By.ID, "name_middle")
    ADD_QNAME = (By.XPATH, "//select[@name='ProfileForm[nameQuality]']")
    ADD_QDOB = (By.ID, "q_dob")
    ADD_DOB = (By.ID, "birth_date")
    ADD_ALIAS = (By.ID, "alias")
    ADD_GENDER = (By.ID, "gender")
    ADD_RACE = (By.XPATH, "//*[contains(text(), '{}')]")
    ADD_ETHNICITY = (By.ID, "ethnicity")
    ADD_SUFFIX_PREFIX = (By.ID, "name_suffix")
    ADD_LANGUAGE = (By.ID, "c_primary_language")
    ADD_RECORD_GO = (By.ID, "form-buttons__btn--submit")
    ADD_RECORD_CANCEL = (By.XPATH, '//a[@href="/client/list"]')

class ClarityClientLocators(object):

    ### Header Links
    CLIENT_NOTES = (By.LINK_TEXT, "Notes")
    CLIENT_PROGRAMS = (By.LINK_TEXT, "Programs")
    CLIENT_ASSESSMENT = (By.LINK_TEXT, "Assessments")

class ClarityClientPrograms(object):
    OUTREACH_NEIGHBORHOOD = (By.XPATH, "//div[@class='name_agency']")

class ClarityEmploymentLocators(object):

    PLACEHOLDER = "okay"


