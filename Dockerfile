FROM python:alpine3.17

RUN apk add curl
RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/ ./
EXPOSE 3000
ENV MONGO_HOSTNAME "mongo"
ENV MONGO_USER ""
ENV MONGO_PASSWORD ""

ENTRYPOINT [ "python3", "app.py" ]