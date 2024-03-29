import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() # Bring up firefox

    def tearDown(self):
        self.browser.quit() # Stops the running test

    def test_home_page(self): 
        # (User Story) A hears about a Todo list website and decideds to visit
        self.browser.get('http:\\localhost:8000') # Get LocalHost page 
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title) 
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)


        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            # Checks to see if search item is in row
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        ) 


        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test')


        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
if __name__ == '__main__':
    unittest.main()
