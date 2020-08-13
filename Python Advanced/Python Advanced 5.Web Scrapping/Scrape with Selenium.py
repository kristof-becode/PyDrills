
# The selenium.webdriver module provides all the implementations of WebDriver. WebDriver implementations
# Currently supported are Firefox, Chrome, IE and Remote. The Keys class provides keys in
# the keyboard such as RETURN, F1, ALT etc.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#!!!!!!!!
#IMPORTANT NOTE TO SELF: extract geckodriver and then copy to usr/bin from where it was extracted to : sudo cp geckodriver /usr/bin
#!!!!!!!!!
def main():
# Then, the instance of Firefox WebDriver is created.
    driver = webdriver.Firefox()
# The driver.get method will lead to a page given by the URL. WebDriver will wait until the page is fully completed
# loaded (i.e. the "onload" event has been triggered) before returning the control to your script.
# It should be noted that if your page uses a lot of AJAX when loading, WebDriver may not know
# when it was fully charged:
    driver.get("http://www.python.org")
# The following line is a statement confirming that the title contains the word "Python"
    assert "Python" in driver.title
# WebDriver offers several methods to search for items using one of the methods
# find_element_by_by_ * . For example, the input text element can be located by its name attribute by
# using the find_element_by_name method
    elem = driver.find_element_by_name("q")
# Then we send keys. This is similar to entering keys using your keyboard.
# Special keys can be sent using the imported selenium.webdriver.common.keys Keys class.
# For security reasons, we will delete any pre-filled text in the input field
# (for example, "Search") so that it does not affect our search results:


    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

#After submitting the page, you should get the result if there is one. To ensure that certain results
# are found, make an assertion:
    assert "No results found." not in driver.page_source
    driver.close()

main()