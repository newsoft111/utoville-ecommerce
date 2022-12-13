# python 버전 or latest 입력
FROM python:3.11.0

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

#RUN apt-get install git -y

RUN mkdir /var/django
ADD . /var/django
#RUN git clone https://github.com/newsoft111/utoville-ecommerce /var/django

WORKDIR /var/django

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "access.log", "--error-logfile", "error.log", "config.wsgi:application"]