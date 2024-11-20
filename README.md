Develop
===

start ORTANC server:
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc```

or with plugins enabled:
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc-plugins:1.12.4```

login web app:
http://localhost:8042/
username: orthanc
password: orthanc

run virtual environment:
```venv\Scripts\Activate.ps1```


Install
===

download and install Docker-Desktop:
- https://www.docker.com/products/docker-desktop/

download docker image (will be automatically done for you):
- https://www.orthanc-server.com/download.php
- https://orthanc.uclouvain.be/book/users/docker.html

download some example files:
- https://www.dicomlibrary.com/

install dependencies:
```python -m pip install -r requirements.txt```

read the docs:
- https://pydicom.github.io/
- https://pydicom.github.io/pydicom
- https://pydicom.github.io/pynetdicom
