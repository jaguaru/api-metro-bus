#### iniciar la imagen base
FROM alpine:3.17

#### instalacion de librerias necesarias para iniciar
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools wheel
RUN apk add --no-cache python3-dev
RUN apk add --no-cache mysql-client
RUN apk add --no-cache py3-mysqlclient
RUN apk add --no-cache libressl-dev
RUN apk add --no-cache libffi-dev libc-dev
RUN apk add --no-cache gfortran gcc g++
RUN apk add --no-cache cython
RUN apk add --no-cache py3-numpy
RUN apk add --no-cache py3-pandas

#### directorio de trabajo actual
WORKDIR /docker-api-metro-bus

#### copia el contenido dentro del directorio de trabajo
ADD . /docker-api-metro-bus

#### instalacion de dependecias mediante pip
RUN pip install -r requirements.txt

#### comandos para iniciar el contenedor
CMD ["python3", "main.py"]

