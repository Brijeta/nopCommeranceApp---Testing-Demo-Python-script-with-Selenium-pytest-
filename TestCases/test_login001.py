import pytest
from selenium import webdriver
from PageObjects.Login_AdminPageObject import Login
from Utilities.readProperties import ReadConfig
from Utilities.cutomLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("**************  Test_001_Login ********************")
        self.logger.info("***********Verifying Home page title **************")
        
        self.driver = setup #get a driver from fixture

        self.driver.get(self.baseURL) #get url
        act_title = self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.logger.info("Home page test case pass")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.Info("Home page test case Fail")
            self.driver.close()
            assert False


    def test_Login(self,setup):
        self.logger.info("***********Verifying Login test case **************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp =Login(self.driver)
        
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********** Login title test case Pass**************")
            self.driver.close()
            assert True
        else:
            self.logger.Info("*********** Login title test case Fail**************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False


