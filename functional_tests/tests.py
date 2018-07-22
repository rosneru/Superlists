# Projekt aus dem Buch:
# "Test-driven development with Python
#
# Erstellt wird eine To-Do-Listen-WebApp 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith hat von einer neuen, coolen Online-App gehört, die 
        # To-Do-Listen verwalten kann. Sie geht gleich mal auf die 
        # Homepage..
        self.browser.get('http://localhost:8000')

        # Sie bemerkt, dass der Seiten-Titel den Text "To-Do" 
        # beinhaltet
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # In eine Textbox kann sie einen ersten To-Do-Eintrag eingeben
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Sie schreibt "Kaufe Pfauenfedern" in die Textbox
        inputbox.send_keys('Kaufe Pfauenfedern')

        # Sobald sie ENTER drückt, wird die Seite aktualisiert und 
        # zeigt nun an "1: Kaufe Pfauenfedern" als ein Eintrag in
        # einer To-Do-Listen-Tabelle
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Kaufe Pfauenfedern')

        # Die Textbox zur Eingabe von To-Do-Einträgen ist immer noch 
        # da. Sie gibt nun ein: "Stelle die Pfauenfedern in eine Vase"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Stelle die Pfauenfedern in eine Vase')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Die Seite aktualisiert sich erneut und zeigt nun beide 
        # Einträge in der To-Do-Liste an
        self.check_for_row_in_list_table('1: Kaufe Pfauenfedern')
        self.check_for_row_in_list_table('2: Stelle die Pfauenfedern in eine Vase')

        # Edith fragt sich, ob die Seite sich ihre Liste merken kann. 
        # Dann bemerkt sie, dass die Seite eine individuelle URL für 
        # sie erstellt hat -- Dazu gibt es auch einen erklärenden Text
        self.fail('Finish the test!')

        # Sie ruft die URL auf - Ihre To-Do-Liste ist noch da.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
