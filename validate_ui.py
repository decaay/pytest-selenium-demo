import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

 
@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass
class Test_URL_Chrome(Basic_Chrome_Test):
        def test_open_url(self):
            self.driver.get("http://localhost:5001")
            print("\n testing \n")
            print(self.driver.find_element_by_tag_name('h1').text)
            assert "It works!" == self.driver.find_element_by_tag_name('h1').text
 
            #sleep(5)