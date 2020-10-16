FROM python:3.6

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install feedparser

ADD . /app

CMD ["python", "bot.py"]
