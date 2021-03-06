# Projekt aus dem Buch:
# "Test-driven development with Python
#
# Erstellt wird eine To-Do-Listen-WebApp 

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Edith hat von einer neuen, coolen Online-App gehört, die 
        # To-Do-Listen verwalten kann. Sie geht gleich mal auf die 
        # Homepage..
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Kaufe Pfauenfedern')

        # Die Textbox zur Eingabe von To-Do-Einträgen ist immer noch 
        # da. Sie gibt nun ein: "Stelle die Pfauenfedern in eine Vase"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Stelle die Pfauenfedern in eine Vase')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Die Seite aktualisiert sich erneut und zeigt nun beide 
        # Einträge in der To-Do-Liste an
        self.wait_for_row_in_list_table('1: Kaufe Pfauenfedern')
        self.wait_for_row_in_list_table('2: Stelle die Pfauenfedern in eine Vase')

        # Edith fragt sich, ob die Seite sich ihre Liste merken kann. 
        # Dann bemerkt sie, dass die Seite eine individuelle URL für 
        # sie erstellt hat -- Dazu gibt es auch einen erklärenden Text
        #self.fail('Finish the test!')

        # Sie ruft die URL auf - Ihre To-Do-Liste ist noch da.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith startet eine neue To-do-Liste
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kaufe Pfauenfedern')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Kaufe Pfauenfedern')

        # Sie bemerkt, dass ihre Liste eine individuelle URL hat
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Nun besucht der neue Benutzer Francis die Seite

        ## Wir starten eine neue Browser-Sitzung um sicherzugehen,
        ## dass keine Information (Cookies etc) aus Ediths Sitzung
        ## wieder verwendet wird
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis besucht die Homepage. Ediths Liste ist nicht zu 
        # sehen
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kaufe Pfauenfedern', page_text)
        self.assertNotIn('Stelle die Pfauenfedern in eine Vase', page_text)

        # Francis startet eine neue Liste, indem er ein neues Item 
        # eingibt
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kaufe Milch')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Kaufe Milch')

        # Francis bekommt seine eigene URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Erneut ist Edith Liste nicht zu sehen
        page_text = self.find_element_by_tag_name('body').text
        self.assertNotIn('Kaufe Pfauenfedern', page_text)
        self.assertIn('Kaufe Milch', page_text)
