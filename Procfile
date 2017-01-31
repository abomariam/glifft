web: gunicorn glifft.wsgi --log-file -
worker: celery worker --beat --app=glifft.celeryapp:app --loglevel info