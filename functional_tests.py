# Projekt aus dem Buch:
# "Test-driven development with Python
#
# Erstellt wird eine TODO-Listen-WebApp 

from selenium import webdriver

browser = webdriver.Firefox()

# Edith hat von einer neuen, coolen online App gehört, die TODO-Listen 
# verwalten kann. Sie geht gleich mal auf die Homepage..
browser.get('http://localhost:8000')

# Sie bemerkt, dass der Seiten-Titel den Text "To-Do" beinhaltet
assert 'To-Do' in browser.title

# In eine Textbox kann sie einen ersten TODO-Eintrag eingeben

# Sie schreibt "Kaufe blaue Pfauenfedern" in eine Textbox

# Sobald sie ENTER drückt, wird die Seite aktualisiert und zeigt nun an
# "1: Kaufe blaue Pfauenfedern" als ein Eintrag in einer TODO-Liste

# Die Textbox zur Eingabe von TODO-Einträgen ist immer noch da. Sie 
# gibt nun ein: "Stelle die Pfauenfedern in eine Vase"

# Die Seite aktualisiert sich erneut und zeigt nun beide Einträge in 
# der TODO-Liste an

# Edith fragt sich, ob die Seite sich wohl ihre Liste merken kann. 
# Dann bemerkt sie, dass die Seite eine individuelle URL für sie 
# erstellt hat -- Dazu gibt es auch einen erklärenden Text

# Sie ruft die individuelle URL auf - Ihre TODO-Liste ist noch da.

# Zufriden geht sie ins Bett und schläfte ein.

browser.quit();
