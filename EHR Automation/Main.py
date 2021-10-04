import unittest
from openpyxl.descriptors.serialisable import KEYWORDS
import pages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC, wait
import openpyxl as xl
from elements import BasePageElement
import locators
import time 


class Agency(unittest.TestCase):

    def setUp(self):
        Clarity = pages.StartUp.clarity_start(self)
        Clarity

    def test_example(self):

        new_client_loop = pages.ClarityCompletes.clarity_new_client_check(self)

        new_client_loop


            
    def tearDown(self):
        time.sleep(5)

if __name__=="__main__":
        unittest.main()
