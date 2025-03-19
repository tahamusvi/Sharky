FROM python:3.11

ADD . /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# RUN mkdir -p /usr/src/app/staticfiles \
#   && python manage.py collectstatic

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000