FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /DjangoReact
WORKDIR /DjangoReact
# Installing OS Dependencies
ADD . /DjangoReact/
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libsqlite3-dev
RUN pip install -U pip setuptools
# COPY requirements.txt /DjangoReact/
RUN pip install -r /DjangoReact/requirements.txt
# Django service
EXPOSE 8000
ENTRYPOINT [ "sh", "run_web.sh" ]