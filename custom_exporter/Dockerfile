FROM python:3.8

WORKDIR /app

COPY onedev_exporter.py /app/

RUN pip install prometheus_client
RUN pip install requests
EXPOSE 9101

CMD [ "python", "custom_exporter.py" ]
