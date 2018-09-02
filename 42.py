pip3 install django
PATH="$PATH:/home/sebastian_colomar/.local/bin"
django-admin.py startproject wisdompets
cd wisdompets
python3 manage.py migrate
python3 manage.py runserver
sudo apt-get install links
links http://localhost:8000
ls -l
python3 manage.py startapp adoptions
cat adoptions/models.py
python3 manage.py makemigrations
python3 manage.py showmigrations
python3 manage.py migrate
