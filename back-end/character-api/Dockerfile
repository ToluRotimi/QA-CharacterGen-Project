FROM python:3.8

WORKDIR /character-api

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5003

ENTRYPOINT ["python3", "app.py"]