cd ..
python -m venv env
call env/scripts/activate



django-admin startproject django_settings .
django-admin startapp django_app
django-admin startapp django_auth

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


cmd
