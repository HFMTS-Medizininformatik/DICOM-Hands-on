Install Project Dependencies
===

1. Setup virtual environment:
```python -m venv .venv```

2. Activate virtual environment:
```.venv\Scripts\Activate.ps1```

3. Update package manager:
```python -m pip install --upgrade pip```

4. Install project dependencies:
```python -m pip install -r requirements.txt```


Setup Open Source PACS (Orthanc)
===

1. Start ORTANC server  
a) ...default:  
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc```  
b) ... with plugins enabled (prefered method):  
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc-plugins:1.12.4```

2. Login to web app: http://localhost:8042/
> Username: `orthanc`  
> Password: `orthanc`


Test DICOM Modality (Python Example)
===

1. Open a new terminal and activate virtual environment, if not already done:  
```.venv\Scripts\Activate.ps1```

2. Login to web app (http://localhost:8042/) and navigate to the `Orthanc Explorer 2` (find the black button at the bottom of the home screen)

> There won't be any study available yet.

3. Run the example project: ```python .\src\main.py```

> * It will print the dicom dataset of an example modality to the terminal
> * And opens a window that shows the pixel image of a corresponding CT

4. Close the window (pixel image) and update the web app and see a new study appear.

5. Click on the eye icon for viewing the pixel image on the web app.

> Read the docs to learn more:
> - https://pydicom.github.io/
> - https://pydicom.github.io/pydicom
> - https://pydicom.github.io/pynetdicom
