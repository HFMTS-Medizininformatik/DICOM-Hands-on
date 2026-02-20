Install
===

1. Setup virtual environment:
```python -m venv venv```

2. Activate virtual environment:
```venv\Scripts\Activate.ps1```

3. Install project dependencies:
```python -m pip install -r requirements.txt```


Setup
===

**1. Open Source PACS (Orthanc)**

Start ORTANC server:  
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc```

... or with plugins enabled (prefered method):  
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc-plugins:1.12.4```

Login to web app: http://localhost:8042/
> Username: `orthanc`  
> Password: `orthanc`


**2. Python Example (DICOM Modality)**

Activate virtual environment, if not already done:  
```venv\Scripts\Activate.ps1```

Run project: ```python .\src\main.py```


> Read the docs:
> - https://pydicom.github.io/
> - https://pydicom.github.io/pydicom
> - https://pydicom.github.io/pynetdicom
