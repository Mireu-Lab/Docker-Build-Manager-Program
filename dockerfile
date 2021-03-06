FROM python:3

RUN mkdir app
WORKDIR /app

COPY . .

RUN pip3 install flask
RUN pip3 install requests

CMD [ "python3", "App/main.py" ]