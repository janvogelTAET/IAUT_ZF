#!/usr/bin/env python3
# Generiert sections/10_register.tex: alphabetisch sortiert, zweispaltig.
import unicodedata, sys

E = [
    ("ADS / AMS Net Id", "sec:twincat"),
    ("Aliasing", "rez:diskret"),
    ("Ampel (MEP)", "bsp:ampel"),
    ("Anti-Reset-Windup", "sec:arw"),
    ("Abtasttheorem", "rez:diskret"),
    (r"\R{AT \%I*} / \R{\%Q*}", "rez:gvlio"),
    ("Automatisierungspyramide", "sec:grundlagen"),
    ("Back-Calculation", "sec:arw"),
    ("Basiszeit", "bsp:tasks"),
    ("Bibliothek", "sec:biblio"),
    ("Butterworth", "bsp:fbfilter"),
    (r"\R{CASE}", "rez:automat"),
    ("CoE / CoE-Startup", "sec:twincat"),
    ("Conditional Integration", "sec:arw"),
    ("D-Anteil gefiltert", "rez:pid"),
    ("Differenzengleichung", "rez:diskret"),
    ("Doppelklick", "bsp:edge"),
    ("DUT", "sec:st"),
    ("EdgeDetector", "bsp:edge"),
    ("EL3004", "sec:twincat"),
    ("EL6900 / EL1904 / EL2904", "sec:safety"),
    ("EN 61499", "sec:sprachen"),
    ("ENUM", "sec:st"),
    ("EtherCAT", "sec:ethercat"),
    ("Euler vorw./rückw.", "rez:diskret"),
    (r"\R{EXIT}", "sec:st"),
    ("Fail-Safe", "sec:safety"),
    ("Feldbus", "sec:feldbus"),
    ("FIR / IIR", "rez:diskret"),
    ("Flanke", "bsp:edge"),
    ("Förderband (MEP)", "bsp:foerderband"),
    ("Forgetting Factor", "sec:mittelwert"),
    ("Freerun / Config", "sec:twincat"),
    ("Funktion / FB / Programm", "sec:pou"),
    ("GVL", "rez:gvlio"),
    ("Hot Connect", "sec:ethercat"),
    ("I-Anteil Trapez", "rez:pid"),
    ("IEC 61131-3", "sec:sprachen"),
    ("IEC 61508 / SIL", "sec:safety"),
    ("Init/Run", "sec:initrun"),
    ("Instanz", "falle:instanz"),
    ("ISO 13849 / PL", "sec:safety"),
    ("Jitter", "sec:tasks"),
    ("Ja/Nein-Fragen", "sec:quiz"),
    ("Mittelwert gleitend", "sec:mittelwert"),
    ("NOVRAM / USV", "sec:remanenz"),
    ("On-the-fly / in-place", "sec:ethercat"),
    ("PAE / PAA", "sec:twincat"),
    ("PERSISTENT", "sec:remanenz"),
    ("PID-Regler", "sec:pid"),
    ("PLCopenXML", "sec:biblio"),
    ("Priorität", "sec:tasks"),
    ("PT1 / PT2", "rez:diskret"),
    ("PT1T2-Strecke", "sec:initrun"),
    ("PWM", "sec:signale"),
    (r"\R{R\_TRIG}", "sec:timer"),
    ("Redundanz 1oo2", "sec:safety"),
    ("RETAIN", "sec:remanenz"),
    ("Route", "sec:twincat"),
    ("Scan-Zyklus", "sec:twincat"),
    ("Schaltschrank", "sec:grundlagen"),
    ("Sensor skalieren", "rez:skalierung"),
    (r"\R{SHL} / \R{SHR}", "rez:statuswort"),
    ("Statuswort", "rez:statuswort"),
    ("Steuern vs. Regeln", "sec:grundlagen"),
    ("STRUCT", "sec:st"),
    ("Sync Unit", "sec:ethercat"),
    ("Task", "sec:tasks"),
    (r"\R{TON} / \R{TOF} / \R{TP}", "sec:timer"),
    ("Tustin", "rez:diskret"),
    ("Typkonvertierung", "sec:st"),
    ("UML-Statechart", "sec:automaten"),
    (r"\R{WHILE}-Falle", "sec:st"),
    ("Working Counter", "sec:ethercat"),
    ("z-Transformation", "rez:diskret"),
    ("Zustandsautomat", "rez:automat"),
    ("Zweierkomplement", "sec:st"),
]


def key(label):
    """Sortierschluessel: LaTeX-Markup weg, Umlaute normalisieren."""
    s = label
    for junk in (r"\R{", r"\T{", "}", "\\", "_"):
        s = s.replace(junk, "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.upper()


E.sort(key=lambda p: key(p[0]))
half = (len(E) + 1) // 2
left, right = E[:half], E[half:]
right += [("", "")] * (len(left) - len(right))

out = [
    "% !TEX root = ../main.tex",
    "% ---------------------------------------------------------------------",
    "%  Stichwortregister -- vom Begriff zur Abschnittsnummer",
    "%  ERZEUGT von mkreg.py. Neue Eintraege dort ergaenzen und neu laufen",
    "%  lassen, oder hier von Hand alphabetisch einsortieren.",
    "% ---------------------------------------------------------------------",
    r"\vlsec{cREF}{REF}{Stichwortregister}",
    "",
    r"\scriptsize",
    r"\begin{tabularx}{\linewidth}{@{}Xr@{\hskip6pt}Xr@{}}",
]
for (la, ra_), (lb, rb) in zip(left, right):
    a = f"{la} & \\ref{{{ra_}}}" if la else " & "
    b = f"{lb} & \\ref{{{rb}}}" if lb else " & "
    out.append(f"{a} & {b} \\\\")
out += [r"\end{tabularx}", r"\normalsize", ""]

with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print(f"{len(E)} Eintraege, {len(left)} Zeilen")
