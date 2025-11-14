# Lösen Sie nachfolgende Aufgaben.
# Bei ### wird das erwartete Ergebnis auf der Konsole angezeigt.
# Nachfolgende Bibliothek os ermöglicht es, dass Konsole immer gelehrt wird
import os
# MacOS und Linux 'clear', Windows 'cls'
os.system('clear' if os.name == 'posix' else 'cls')


# Aufgabe 1: 
print("\nAufgabe 1:")
print("Analysieren Sie das folgende Verhalten:")
print("Welche Schlussfolgerung ziehen Sie aus dem Verhalten?")
text1 = "Text"
print("Text1 ist vom Datentyp:", type(text1), "und hat den Inhalt", text1)
text1 = 2
print("Text1 ist vom Datentyp:", type(text1), "und hat den Inhalt", text1)
text1 = True
print("Text1 ist vom Datentyp:", type(text1), "und hat den Inhalt", text1)



# -----------------------------------------------------------------------------

# Aufgabe 2
#Folgende Liste ist gegeben 
einkaufen = ["Brot", 5, "Äpfel", "Eier"] 

## Aufgabe 2a
print("\nAufgabe 2a:")
print("Ausgabe des Arrayinhalts:")
### ['Brot', 5, 'Äpfel', 'Eier']
print(einkaufen)


## Aufgabe 2b
print("\nAufgabe 2b: ")
print("Ausgabe der Listeneinträge untereinander:") 
### Brot
### 5
### Äpfel
### Eier

for item in einkaufen:
    print(item)


## Aufgabe 2c
print("\nAufgabe 2c: ")
print("Einfügen des Wertes 'Salat' nach 'Äpfel'")
### ['Brot', 5, 'Äpfel', 'Salat', 'Eier']
einkaufen.insert(3, "Salat")
print(einkaufen)


## Aufgabe 2d
print("\nAufgabe 2d: ")
print("Löschen des Eintrags '5' aus der Liste 'einkaufen'")
### Ergebnis: ['Brot', 'Äpfel', 'Salat', 'Eier']
einkaufen.remove(5)
print(einkaufen)




# -----------------------------------------------------------------------------

# Aufgabe 3
## Aufgabe 3a
print("\nAufgabe 3a: ")
print("Durchlaufen der Liste einkaufen mit Foreach Schleife")

for item in einkaufen:
    print(item)

## Aufgabe 3b
print("\nAufgabe 3b: ")
print("Durchlaufen der Liste einkaufen mit einer zählergesteuerten Schleife")

for item in range(4):
    print(einkaufen[item])


## Aufgabe 3c
print("\nAufgabe 3c: ")
print("Durchlaufen der Liste einkaufen mit While Schleife")

index = 0
while index < len(einkaufen):
    print(einkaufen[index])
    index += 1


# -----------------------------------------------------------------------------

# Aufgabe 4
## Aufgabe 4a
print("\nAufgabe 4a: ")
text = "Welt"
print("Verwende Variable Text um auf der Konsole 'Hallo Welt' auszugeben.")
# Für diese Aufgabe gibt es mehrere Lösungsvarianten

print("Hallo ", text)

## Aufgabe 4b
print("\nAufgabe 4b: ")
zahl = 2
print("Verwende Variable Zahl um auf der Konsole '2 Personen' auszugeben.")

print(zahl, "Personen")

# -----------------------------------------------------------------------------

## Aufgabe 5
print("\nAufgabe 5: ")
person1 = "Kai"
person2 = "Tom"
print(person1, person2) 
print("Austausch Person1 mit Person2 und das Ergebnis auf der Konsole ausgeben")
### Tom Kai

x = person1
person1 = person2
person2 = x

print("Person1: ", person1)
print("Person2: ", person2)



# -----------------------------------------------------------------------------

## Aufgabe 6
print("\nAufgabe 6: ")
print("Erstelle einen Userdialog mit der Möglichkeit ein Ergebnis einzutragen -> (Ergebnis: )")
print("Wenn Ergebnis Zahl 1 ist, dann Ausgabe 'super'")
print("Wenn Ergebnis Zahl 2 ist, dann Ausgabe 'gut'")
print("Ansonsten 'Fehler'")
### Ergebnis: 2
### gut

zahl = int(input("Ergebnis: "))
if zahl == 2: print("gut")
elif zahl == 1: print("super")
else:
    print("'Fehler'")


# -----------------------------------------------------------------------------

## Aufgabe 7
print("\nAufgabe 7: ")
print("Erstelle eine Funktion 'formatierteAusgabe'") 
print("Funktion erhält zwei Übergabeparameter die ausgegeben werden sollen")
print("Orientieren Sie sich am beispielhaften Aufruf")
level = 40
nickname = "Mat"
# formatierteAusgabe("Nickname", nickname)
# formatierteAusgabe("Level", level)
### +++ Nickname +++  
### Mat
### +++ Level +++  
### 40

def formatierteAusgabe(nickname, level):
    print("+++ Nickname +++ \n", nickname)
    print("+++ Level +++ \n", level)

formatierteAusgabe(nickname, level)
