FROM python:3.12
ENV PYTHONBUFFERED 1

WORKDIR /midterm_djangohotdog
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python ./manage.py runserver 0.0.0.0.8000