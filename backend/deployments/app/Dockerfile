FROM python:3
ADD app/ /app
WORKDIR /app
run apt-get update
RUN pip3 install -r requirements.txt
CMD python app.py

