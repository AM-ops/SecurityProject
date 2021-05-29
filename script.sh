source activate myDjangoEnv
python manage.py makemigrations
python manage.py migrate
xdg-open http://127.0.0.1:8000
python manage.py runserver
