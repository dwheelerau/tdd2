from selenium import webdriver
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_latter(self):
        # Edith has head about a cool online to-do app she checks it out
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists.
        assert 'To-Do' in self.browser.title
        self.fail("Finish the tests!")

        # She is invited to enter a list

        # She types "buy peacock feathers" into a text box

        # When she hits enter the page updates and now th epage lists
        # 1: Buy peacock feathers as an item on the todo list.

        # There is still a text box inviting her to add another item
        # She enter "use peacock feathers to make a fly"

        # The page updates again and shows both items.

        # Edith wonders if the site will remember her list. She sees
        # It has generated a unique url for her
        # There is some explanation text that describes this.

        # She visits this url and her list is there.

        # Satisfied she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
