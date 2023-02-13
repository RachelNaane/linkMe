FROM python:alpine3.17

RUN apk add curl

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/ ./
EXPOSE 3000
ENV MONGO_HOSTNAME ""
ENV MONGO_USER ""
ENV MONGO_PASSWORD ""

ENTRYPOINT [ "python3", "app.py" ]