FROM python:3.8

WORKDIR /app

COPY custom_exporter.py .

RUN pip install prometheus_client
RUN pip install requests
EXPOSE 9101

CMD [ "python", "custom_exporter.py" ]
