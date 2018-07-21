# Detect the languages present in the given sentence

This work detects the given language/languages present in the given sentence.

### Requirements

```
* python >=3.4
* lang_detect
* polyglot
* flask (only if you want to host using flask)
* docker (only if you want to host it using docker)

```

### Installation

* git clone https://github.com/kumar-shridhar/Detect-Language.git
* cd Detect-Language
* pip install -r requirements.txt

### Usage

```
detect_language.py [-h]  [--str String]
               [--supported_language, --sl]

** required arguements:
  --str                           string to detect language


** optional arguments:
  -h, --help                      help message
  --sl, --supported_language      supported languages

```
### Host using Flask


```
python flask_hosted/app.py

```

Default port used is localhost:8082

### Host using Flask


```
docker build docker/Dockerfile 

```

NOTE: Docker needs to be installed before using it with docker. Install docker from here for Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/ 

### Run tests


```
python tests/test.py

```


