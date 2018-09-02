pip3 install django
PATH="$PATH:/home/sebastian_colomar/.local/bin"
django-admin.py startproject wisdompets
cd wisdompets
python3 manage.py startapp adoptions
cat adoptions/models.py
cat adoptions/admin.py
grep ALLOWED_HOSTS wisdompets/settings.py
python3 manage.py makemigrations
python3 manage.py showmigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py load_pet_data
python3 manage.py runserver 0.0.0.0:8000
