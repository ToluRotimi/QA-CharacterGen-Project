FROM python:3.8

WORKDIR /colour-api

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ["python3", "app.py"]