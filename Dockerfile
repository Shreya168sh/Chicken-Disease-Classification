FROM python:3.10.8-slim-buster

RUN apt update -y
WORKDIR . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]