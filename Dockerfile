FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY ./requirements.txt /code
RUN pip install -r requirements.txt
