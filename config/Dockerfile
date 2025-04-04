FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

RUN mkdir -p /usr/src/app/staticfiles \
  && python manage.py collectstatic

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000