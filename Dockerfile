FROM python:3.10

EXPOSE 8000

RUN apt-get update && apt-get install
RUN apt-get install -y libpq-dev
RUN apt install curl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH $PYTHONPATH:/usr/src/app

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]