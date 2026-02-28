# DICOM Hands-on

**Inhaltsverzeichniss:**

-   Projektabhängigkeiten installieren
-   Open-Source-PACS (Orthanc) einrichten
-   DICOM-Modality testen (Python-Beispiel)
-   Weiterführende Dokumentation


## Projektabhängigkeiten installieren

### 1. Virtuelle Umgebung einrichten

Erstellen Sie zunächst eine virtuelle Python-Umgebung:

``` bash
python -m venv .venv
```

### 2. Virtuelle Umgebung aktivieren (Windows PowerShell)

``` bash
.venv\Scripts\Activate.ps1
```

> Achtung: Nach der Aktivierung sollte `(.venv)` am Anfang der Kommandozeile erscheinen.

### 3. Paketmanager (pip) aktualisieren

``` bash
python -m pip install --upgrade pip
```

### 4. Projektabhängigkeiten installieren

``` bash
python -m pip install -r requirements.txt
```


## Open-Source-PACS (Orthanc) einrichten

Für dieses Projekt wird der DICOM-Server **Orthanc** als PACS
verwendet.\
Der Server wird bequem per Docker gestartet.

### 1. Orthanc-Server starten

#### a) Standardversion

``` bash
docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc
```

#### b) Mit aktivierten Plugins (empfohlene Variante)

``` bash
docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc-plugins:1.12.4
```

**Erklärung der Ports:** 

-   `4242` → DICOM-Port (C-STORE, C-ECHO etc.)  
-   `8042` → Weboberfläche

### 2. Anmeldung an der Weboberfläche

http://localhost:8042/

> **Zugangsdaten:**  
> 
> Benutzername: `orthanc`  
> Passwort: `orthanc`  


## DICOM-Modality testen (Python-Beispiel)

### 1. Neues Terminal öffnen & virtuelle Umgebung aktivieren

``` bash
.venv\Scripts\Activate.ps1
```

### 2. Orthanc-Weboberfläche öffnen

http://localhost:8042/

Klicken Sie auf den schwarzen Button **„Orthanc Explorer 2"** am unteren
Rand der Startseite.

> Hinweis: Zu diesem Zeitpunkt wird noch keine Studie aufgelistet.

### 3. Beispielprojekt ausführen

``` bash
python .\src\main.py
```

**Erwartetes Verhalten:**

-   Das DICOM-Dataset einer Beispiel-Modality wird im Terminal
    ausgegeben.
-   Zusätzlich öffnet sich ein Fenster mit der Pixel-Darstellung eines
    CT-Bildes.

### 4. Bildfenster schliessen

Schliessen Sie das geöffnete Bildfenster und aktualisieren Sie anschliessend die Weboberfläche.

> Hinweis: Nun sollte eine neue Studie in Orthanc erscheinen.

### 5. Studie im Webviewer anzeigen

Klicken Sie auf das **Augen-Symbol**, um das Bild zu betrachten.


## Weiterführende Dokumentation

-   https://pydicom.github.io/
-   https://pydicom.github.io/pydicom
-   https://pydicom.github.io/pynetdicom