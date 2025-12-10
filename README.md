# Hangman

Hangman ist ein klassisches Wortspiel für 2 - 5 Spieler, das darauf abzielt, ein verstecktes Wort durch das Erraten einzelner Buchstaben aufzudecken.
Über eine einfache und übersichtliche Oberfläche können Spieler einen Buchstaben nach dem anderen auswählen und sehen, ob dieser im gesuchten Wort vorkommt.
Das Spiel zeigt jederzeit den aktuellen Fortschritt, die bereits geratenen Buchstaben sowie die verbleibenden Versuche an.
Ziel ist es, das vollständige Wort zu erraten, bevor alle Fehlversuche verbraucht sind.

## Usage
 
Run `uv run main.py`

## Development
 
Das Projekt nutzt den Python-Manager [uv](https://docs.astral.sh/uv/) zur Verwaltung des Projekts.
 
Die Softwarearchitektur ist an das drei Schichten Modell angelehnt.
 
- Datenzugriff / Repository
- Logik / Service
- Anzeige / UI
 
Damit die drei Schichten auch vernünftig miteinander arbeiten können, muss ein gemeinsammes Datenmodell existieren wie Daten ausgetauscht werden.
uv
uv is an extremely fast Python package and project manager, written in Rust.

### Datenspeicher
 
Die Wörter zum eraten befinden sich in einer Text-Datei wörter.txt und sind dort gespeichert.
  
Der Code zum Zugriff auf die Daten als txt befindet sich im **Modul** `repo_txt.py`
-> wird von Aron erstellt
 
### Logik
 
Die Logik Schicht soll die Kommunikation zwischen Datenzugriff und Anzeige übernehmen.
Außerdem sollen hier die Funktionen zur Verwaltung des Spieles implementiert werden.
  
Aktuell befindet sich die Logik in der `main.py` Datei.
-> wird von Marcus erstellt
 
### Oberfläche
 
Als Oberfläche wird in erster Iteration eine kleine TUI Anwendung realisiert. Ein wechsel auf eine grafische Oberfläche ist für die Zukunft geplant.
 
Der Code zur Oberfläche befindet sich im Modul `tui.py`
-> wird von Aron erstellt

### Special

Folgende Funktionen werden realisiert:

- „eingabe_Spieler“
- „hangman_zeichen“
- „wort_darstellen“
- „wort_erzeugen“
- „buchstaben_raten“
- "open_file"
