FROM python:3.8-alpine

  RUN apk add --no-cache jpeg-dev zlib-dev
  RUN apk add --no-cache --virtual .build-deps build-base linux-headers && pip3 install Django==3.0.6 && pip3 install Pillow  && pip3 install django-crispy-forms && pip3 install pylint
