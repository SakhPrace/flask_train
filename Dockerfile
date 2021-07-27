FROM ubuntu:latest
MAINTAINER Vitali Kostyrenko 'vi_ko97@mail.ru'
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["./venv/bin/python", "./app.py"]
EXPOSE 5000