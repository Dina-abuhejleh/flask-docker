FROM python:latest
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get -y install cron
ENTRYPOINT ["sh" , "manage.sh"]
