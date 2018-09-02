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
sudo iptables -t nat -A PREROUTING -d 142.93.169.43/32 -i eth0 -p tcp -m tcp --dport 80 -j DNAT --to-destination 142.93.169.43:8000
sudo iptables -t nat -A POSTROUTING -s 142.93.169.43/32 -o eth0 -p tcp -m tcp --sport 8000 -j MASQUERADE
