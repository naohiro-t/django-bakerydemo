release: yes "yes" | python manage.py migrate
web: uwsgi --http-socket=:$PORT --master --workers=1 --threads=4 --die-on-term --wsgi-file=bakerydemo/wsgi_production.py  --static-map /media/=/app/bakerydemo/media/ --offload-threads 1
