FROM python:3.6.7-slim-stretch

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

RUN mkdir -p /var/www/spaceag
WORKDIR /var/www/spaceag

COPY ./ .

RUN pip install -r requirements/dev.txt
RUN pip install honcho

ENTRYPOINT ["honcho", "start", "-f", "/var/www/spaceag/configuration/development/Procfile", "-e", "/var/www/spaceag/configuration/development/environment"]
