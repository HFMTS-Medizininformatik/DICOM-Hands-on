Dev
===

run venv:
```venv\Scripts\Activate.ps1```


Test
===

https://orthanc.uclouvain.be/book/users/docker.html

start ORTANC server:
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc:1.12.4```

login web app:
http://localhost:8042/
username: orthanc
password: orthanc

with plugins enabled:
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc-plugins:1.12.4```

with orthanc-python:
```docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc-python:1.12.4```
