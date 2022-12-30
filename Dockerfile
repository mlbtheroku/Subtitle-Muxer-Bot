FROM python:3.10.5-slim-buster

WORKDIR .

COPY . .

RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "muxbot.py"]
