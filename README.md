# IAUT Automatisierung Zusammenfassung (HS26) – LaTeX-Quelle

Blöcke B1–B8 für die MEP IAUT (Teil Automatisierung). A4 hoch, 2 Spalten, 8pt, aktuell 6 Seiten.
Die MEP erlaubt alle Unterlagen in Papierform, es gibt also kein Seitenlimit.

## Bauen
- **`IAUT_ZF.code-workspace` mit VS Code öffnen** (Doppelklick oder *Datei → Arbeitsbereich aus Datei öffnen*).
  Darin sind alle LaTeX-Workshop-Einstellungen: Auto-Build beim Speichern, 2× pdflatex, PDF im VS-Code-Tab.
  VS Code fragt beim ersten Öffnen, ob du dem Ordner vertraust → *Ja*. Fehlt LaTeX Workshop, schlägt VS Code die Installation vor.
- Jede Datei in `sections/` hat `% !TEX root = ../main.tex`, Speichern in einem Kapitel baut also immer das ganze Dokument.
- `main.tex` öffnen und speichern → baut automatisch (2× pdflatex). PDF anzeigen: `Ctrl+Alt+V`.
- Ohne VS Code: `pdflatex main.tex` zweimal ausführen, oder `latexmk -pdf main.tex`.

## Struktur
| Datei | Inhalt |
|---|---|
| `main.tex` | Layout (A4 hoch, 2 Spalten), Farben, Boxen, ST-Syntax für `lstlisting`, Kopf/Fuss, Titel + Inhaltsverzeichnis |
| `sections/00_navigation.tex` | Farblegende, MEP-Regeln, Tabelle „Wenn die Aufgabe lautet …“ |
| `sections/01_grundlagen.tex` | B1: Automatisierung, Pyramide, Steuern/Regeln, Feldbusse, IEC-61131-3-Sprachen |
| `sections/02_twincat.tex` | B2: Scan-Zyklus, TwinCAT-Ablauf, `AT %I*/%Q*`, Projektstruktur, ADS, CoE, Remanenz |
| `sections/03_st.tex` | B3: POU-Typen, Datentypen, Kontrollstrukturen, ENUM/STRUCT, Bitoperationen, Timer, EdgeDetector |
| `sections/04_filter.tex` | B4: Sensor skalieren, Testsignale/PWM, Mittelwert, Forgetting Factor, Diskretisierung, Butterworth (MEP) |
| `sections/05_automaten.tex` | B5: Zustandsautomaten, ENUM+CASE-Schema, Förderband und Ampel (MEP HS24) komplett |
| `sections/06_tasks.tex` | B6: Tasks, Prioritäten, Basiszeit, EtherCAT, WC, Sync Units |
| `sections/07_pid.tex` | B7: PID diskretisieren, PT1T2-Strecke, Init/Run, PID-FB, Anti-Reset-Windup |
| `sections/08_safety.tex` | B8: SIL/PL, Redundanz, TwinSAFE-Klemmen |
| `sections/09_referenz.tex` | Ja/Nein-Fragebogen HS24 mit Begründung, alle Formeln, Checkliste für Code auf Papier |
| `sections/10_register.tex` | Stichwortregister (erzeugt, siehe unten) |
| `figures/` | Bilder (PNG), via `\fig{...}` |

Reihenfolge ändern: `\input`-Zeilen in `main.tex` umsortieren.
Block weglassen: Zeile auskommentieren.

## Wie man etwas findet
1. **Farbe** – jeder Block hat eine eigene Balkenfarbe (B1 blau … B8 magenta).
2. **Abschnitt 10** – Stichwortregister, 77 Begriffe → Abschnittsnummer.
3. **Seite 1** – Tabelle „Wenn die Aufgabe lautet …“ geht von der Aufgabenstellung direkt zur Nummer.

## Eigene Befehle (in `main.tex` definiert)
- `\vlsec{cB3}{B3}{Titel}` – Blocküberschrift, setzt zugleich die Blockfarbe
- `\R{VAR_OUTPUT}` – Variable, Schlüsselwort, Code inline (Monospace; `_`, `%`, `#` escapen)
- `\T{Begriff}` – Schlüsselbegriff (fett)
- `\SW{Stichwort}` – farbiges Stichwort am Zeilenanfang, macht die Seite scanbar
- `\ra` – Pfeil mit passenden Abständen
- `\JA` / `\NEIN` – farbige Antwort im Fragebogen
- `\begin{ztab}{@{}Xr@{}} Kopf & Kopf \\ \midrule … \end{ztab}` – kompakte Tabelle über die Spaltenbreite
- `\begin{formel}[Titel] … \end{formel}` – Formel/Kernaussage, färbt sich mit dem Block
- `\begin{falle}[Titel] … \end{falle}` – typischer Fehler (rot)
- `\begin{rezept}[Titel] … \end{rezept}` – Schritt für Schritt (grün)
- `\begin{bsp}[Titel] … \end{bsp}` – durchgerechnetes Beispiel (gelb)
- `\begin{lstlisting} … \end{lstlisting}` – ST-Code mit Syntaxfarben (Sprache `ST` in `main.tex`)
- `\fig[0.6]{name}` – Bild aus `figures/`, Breite als Anteil der Spaltenbreite

## Stichwortregister
`sections/10_register.tex` ist von `mkreg.py` erzeugt (liegt im selben Ordner).
Neue Einträge dort in die Liste `E` eintragen und

```
python mkreg.py sections/10_register.tex
```

laufen lassen – sortiert alphabetisch und verteilt auf zwei Spaltenpaare.
Von Hand einsortieren geht genauso, die Datei ist normales LaTeX.

## Platz
Reicht der Platz nicht:
1. Ränder in `main.tex` (`geometry`) enger,
2. dann die Schriftgrösse in `\documentclass[8pt]{extarticle}` (erlaubt: 8, 9, 10, 11, 12, 14, 17, 20pt),
3. zuletzt Inhalt kürzen.

## Abhängigkeiten
Standardpakete einer vollen TeX-Distribution. Nicht ganz minimal sind
`extsizes` (für `extarticle`), `tcolorbox`, `environ`, `titlesec`,
`lastpage`, `tikz` (Zustandsdiagramm). MiKTeX installiert sie beim ersten Build automatisch nach.

## Stand der Quellen
`IAS_Skript_v1.4` (Kap. 1–10, Anhänge A–F), `IAS_Labor_Aufgabenserie1–8` (7 in v3),
`IAS_SPSProgrammierung_Folien`, `IAS_ReglerDiskretisierung_Folien`,
`DigitaleRegelungSkript` (Kap. 2–4), `MEP__IAUT__HS24`, `IAUT_Automation_MusterPruefung`,
Musterlösungen Aufgabenserie 2 und 3, Laborversuch Drehzahl.

## Zu prüfen
- Fragebogen HS24, Frage 10 (Zykluszeit mehrere Sekunden): in den Unterlagen nicht belegt, als „(Ja?)“ markiert.
- Forgetting Factor: die Aufgabe schreibt `(1−λ)·y(k−1)`, die Herleitung ergibt `(1−λ)·y(k)` (um einen Schritt verschobener Index).
- Ampel HS24: Mit zwei Ampeln dauert Rot = Grün + Gelb der Gegenrichtung = 13 s, nicht 10 s wie in der Aufgabe.
- Die Lösungen zu MEP HS24 (Förderband, Ampel, Butterworth) sind eigene Lösungen, keine offiziellen Musterlösungen.
