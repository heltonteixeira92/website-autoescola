release: python manage.py migrate --noinput
web: gunicorn malves.wsgi --timeout 60 --keep-alive 5 --log-level debug --log-file -