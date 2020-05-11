FROM python:3.8-alpine

  RUN apk add --no-cache jpeg-dev zlib-dev
  RUN apk add --no-cache python3.8 -m pip install Django
  RUN apk add --no-cache --virtual .build-deps build-base linux-headers && pip3 install Pillow  && pip3 install django-crispy-forms 
