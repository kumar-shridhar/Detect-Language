FROM python:3.5

ENV PATH=/root/.local/bin:$PATH

RUN git clone https://github.com/kumar-shridhar/Detect-Language.git
WORKDIR /Detect-Language

RUN pip install -r requirements.txt

ENTRYPOINT python flask_hosted/app.py
