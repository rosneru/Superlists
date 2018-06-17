# Projekt aus dem Buch:
# "Test-driven development with Python
#
# Erstellt wird eine To-Do-Listen-WebApp 

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith hat von einer neuen, coolen online App gehört, die 
        # To-Do-Listen verwalten kann. Sie geht gleich mal auf die 
        # Homepage..
        self.browser.get('http://localhost:8000')

        # Sie bemerkt, dass der Seiten-Titel den Text "To-Do" 
        # beinhaltet
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test.')

        # In eine Textbox kann sie einen ersten To-Do-Eintrag eingeben

        # Sie schreibt "Kaufe blaue Pfauenfedern" in die Textbox

        # Sobald sie ENTER drückt, wird die Seite aktualisiert und 
        # zeigt nun an "1: Kaufe blaue Pfauenfedern" als ein Eintrag 
        # in einer To-Do-Liste

        # Die Textbox zur Eingabe von To-Do-Einträgen ist immer noch 
        # da. Sie gibt nun ein: "Stelle die Pfauenfedern in eine Vase"

        # Die Seite aktualisiert sich erneut und zeigt nun beide 
        # Einträge in der To-Do-Liste an

        # Edith fragt sich, ob die Seite sich ihre Liste merken kann. 
        # Dann bemerkt sie, dass die Seite eine individuelle URL für sie 
        # erstellt hat -- Dazu gibt es auch einen erklärenden Text

        # Sie ruft die URL auf - Ihre To-Do-Liste ist noch da.

if __name__ == '__main__':
    unittest.main(warnings='ignore')