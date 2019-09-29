import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() # Bring up firefox

    def tearDown(self):
        self.browser.quit() # Stops the running test

    def test_home_page(self): 
        # (User Story) Joe hears about a Todo list website and decideds to visit
        self.browser.get('http:\\localhost:8000') # Get LocalHost page 
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title) 
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-do', header.text)


        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
if __name__ == '__main__':
    unittest.main()
