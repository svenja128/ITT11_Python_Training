"""
Projektbeschreibung
Du entwickelst ein Programm zur Verwaltung von Hardware-Komponenten im IT-Labor der Schule. Das System soll Sensoren, Aktoren, Raspberry Pis, Router und andere Komponenten verwalten können.

Jede Komponente hat folgende Eigenschaften:
- Bezeichnung (z.B. "Raspberry Pi 4", "DHT22 Temperatursensor", "LED rot 5mm")
- Menge (verfügbare Stückzahl)
"""


def zeige_menu():
    """Zeigt das Hauptmenü der Hardware-Verwaltung an."""
    print("\n=== HARDWARE-VERWALTUNG ===")
    print("1 - Komponente hinzufügen")
    print("2 - Alle Komponenten anzeigen")
    print("3 - Komponente suchen")
    print("4 - Menge ändern")
    print("5 - Komponente löschen")
    print("6 - Programm beenden")


def main():
    """Hauptprogramm mit Menüschleife."""
    print("Willkommen zur Hardware-Verwaltung!")

    # Endlosschleife für das Menü. Zeigt Funktion zeige_menu() an und wird durch "Programm beenden" unterbrochen. Je nach Auswahl erscheint ein Text, dass die Funktion xy später implementiert wird.
    while True:
        zeige_menu()
        auswahl = input("Bitte eine Option auswählen (1-6): ")
        if auswahl == "1":
            print("Funktion 'Komponente hinzufügen' ausgewählt.")
            komponente_hinzufuegen()
        elif auswahl == "2":
            print("Funktion 'Alle Komponenten anzeigen' ausgewählt.")
        elif auswahl == "3":
            print("Funktion 'Komponente suchen' ausgewählt.")
        elif auswahl == "4":
            print("Funktion 'Menge ändern' ausgewählt.")
        elif auswahl == "5":
            print("Funktion 'Komponente löschen' ausgewählt.")
        elif auswahl == "6":
            print("Programm wird beendet")
            break
        else:
            print("Ungültige Eingabe, bitte eine Zahl zwischen 1 und 6 eingeben.")



# ----------------------------------------------------------------------------
# Komponenten hinzufügen
# ----------------------------------------------------------------------------

# leeres Array für Komponenten anlegen
komponenten = []

# function um komponenten hinzuzufügen
def komponente_hinzufuegen():
    while True:
        komponente_input = input("Komponente eingeben: ")
        menge_input = input("Menge eingeben: ")
        komponente_dict = {
            "komponente": komponente_input,
            "menge": menge_input
        }
        komponenten.append(komponente_dict)
        
        entscheidung = input("Weitere Komponente eingeben? (y/n): ")
        if entscheidung.lower() != "y":
            break



# ----------------------------------------------------------------------------
# Alle Komponenten anzeigen
# ----------------------------------------------------------------------------




# Programm starten (F5 in VS Code)
if __name__ == "__main__":
    main()

