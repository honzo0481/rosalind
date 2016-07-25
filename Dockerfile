FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install --upgrade pip
ADD . /code/
WORKDIR /code
