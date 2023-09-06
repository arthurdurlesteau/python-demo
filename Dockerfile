FROM python:alpine3.18

RUN apk add --update py-pip; \
    apk update; \
    apk add py-pip; \
    pip install --upgrade pip

RUN pip install inputimeout pathlib

RUN mkdir -p /opt/app
ADD ./document_analyzer.py /opt/app/

CMD ["python", "/opt/app/document_analyzer.py"]