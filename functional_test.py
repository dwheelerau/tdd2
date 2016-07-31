from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter the page updates and now th epage lists
        # 1: Buy peacock feathers as an item on the todo list.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in the table"
        )
        # There is still a text box inviting her to add another item
        # She enter "use peacock feathers to make a fly"
        self.fail('finish the tests!')

        # The page updates again and shows both items.

        # Edith wonders if the site will remember her list. She sees
        # It has generated a unique url for her
        # There is some explanation text that describes this.

        # She visits this url and her list is there.

        # Satisfied she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
