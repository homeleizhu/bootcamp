FROM python:alpine
RUN mkdir /code
WORKDIR /code
RUN pip install -U pip

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
