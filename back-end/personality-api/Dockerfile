FROM python:3.8

WORKDIR /personality-api

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["python3", "app.py"]