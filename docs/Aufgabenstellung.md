# Projektaufgabe: ETL-Pipeline für Motorradteile

## 1. Ausgangssituation

Ein Händler für Motorradteile verfügt über verschiedene Datenquellen, aus denen Produkt- und Fahrzeugdaten zusammengeführt werden sollen.

Die vorhandenen Daten liegen als Dateien vor. Die Daten besitzen unterschiedliche Strukturen und teilweise unterschiedliche Schreibweisen.

Ziel des Projektes ist es, eine automatisierte ETL-Pipeline zu entwickeln, die die vorhandenen Daten einliest,  aufbereitet und anschließend in eine Zieldatenbank bzw. ein definiertes Zielformat überführt.

Die Lösung soll so aufgebaut sein, dass sie später regelmäßig und möglichst automatisiert ausgeführt werden kann.

## 2. Projektziel

Entwickeln Sie eine Python-Anwendung, die einen vollständigen ETL-Prozess für Motorrad- und Produktdaten realisiert.

Der Prozess soll aus den drei Phasen bestehen:

Extract -> Transform -> Load

- Daten aus unterschiedlichen Datei-Quellen einlesen
- Analysieren, bereinigen, transformieren, auf Fehler und Inkonsistenz prüfen  
- Die Daten in eine Datenbank schreiben

## 3. Phase 1 – Analyse

Analysieren Sie zunächst die zur Verfügung gestellten Daten.

Untersuchen Sie unter anderem:

- Welche Datenquellen stehen zur Verfügung?
- Welche Tabellen bzw. Dateien gibt es?
- Welche Spalten enthalten die Daten?
- Welche Datentypen werden verwendet?
- Welche Felder können miteinander verknüpft werden?
- Gibt es doppelte Datensätze?
- Gibt es fehlende Werte?
- Gibt es unterschiedliche Schreibweisen?
- Gibt es fehlerhafte oder ungültige Daten?

Überlegen Sie den Datenfluss von den einzelnen Dateien zu der Datenbank.

Dokumentieren Sie Ihre Ergebnisse.  
- Datenanalyse 
- Datenflussplan
- Scriptübersicht / Anforderungen

## 4. Phase 2 - Planung der Architektur 

Planung und Strukturierung des Python Projektes

Folgende Anforderungen:

- Ablegen der Konfiguration als JSON
- Prozess als Konsolenausgabe und gleichzeitiges loggen in einer Datei 
- Objektorientierte Lösung

Folgende Dokumente sollten erstellt werden:
- UML-Anwendungsfalldiagramm
- UML-Klassendiagramm (ETL Komponenten)

## 5. Phase 3 - Implementierung in Python

**Module**
- ABC 
- pandas  
- logging
- sqlalchemy
- os
- json

Anforderungen
- Die Lösung soll Objektorientiert umgesetzt werden.
- Es soll eine main Datei geben die alle Pipelines auf einmal ausführt.
- 


