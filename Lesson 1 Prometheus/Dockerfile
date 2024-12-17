FROM python:3.14.0a2-alpine3.21
WORKDIR /app
RUN pip3 install prometheus_client flask
COPY . .
EXPOSE 5001
CMD ["python", "exporter.py"]