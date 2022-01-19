FROM python:3

RUN mkdir /site
COPY . /site/
WORKDIR /site

RUN pip install django
RUN pip install pillow

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]