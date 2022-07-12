FROM python:3.10

EXPOSE 5000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH $PYTHONPATH:/usr/src/app

COPY . /usr/src/app/

RUN pip install psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]