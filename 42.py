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


django-admin.py startproject cineteca&&cd cineteca
python3 manage.py startapp peliculas
sed -i "/ALLOWED/s/\[\]/\['django.gotdns.org'\]/" cineteca/settings.py
x=django.contrib.admin;sed -i "/$x/s/^\(\s\+\)'"$x"',/\1'peliculas',\n\1'"$x"',/" cineteca/settings.py
sed -i "/^from.*path/s/$/,re_path/" cineteca/urls.py
sed -i "/^from django.urls/afrom peliculas import views" cineteca/urls.py
sed -i "/admin.site.urls/s/^\(\s\+\)\(path.*$\)/\1\2\n\1path('',views.home,name='home'),/" cineteca/urls.py
sed -i "/admin.site.urls/s/^\(\s\+\)\(path.*$\)/\1\2\n\1re_path('peliculas\/(\\\d+)',views.detalles,name='peliculas'),/" cineteca/urls.py

echo -e "\nclass Pelicula(models.Model):">> peliculas/models.py
echo -e "\tGENEROS=[('C','Comedia'),('D','Drama'),('T','Terror')]">> peliculas/models.py
echo -e "\ttitulo=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tdirector=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tactor_principal=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tgenero=models.CharField(choices=GENEROS,max_length=1)">> peliculas/models.py
echo -e "\tpais=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tfecha_estreno=models.DateTimeField()">> peliculas/models.py
echo -e "\tcomentarios=models.TextField()">> peliculas/models.py
echo -e "\tpremios=models.ManyToManyField('Premio',blank=True)">> peliculas/models.py
echo -e "\nclass Premio(models.Model):">> peliculas/models.py
echo -e "\tpremio=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tdef __str__(self):return self.premio">> peliculas/models.py
echo -e "\nfrom .models import Pelicula">> peliculas/admin.py
echo -e "\n@admin.register(Pelicula)">> peliculas/admin.py
echo -e "\nclass GestionPeliculas(admin.ModelAdmin):">> peliculas/admin.py
echo -e "\tlista=['titulo','director','actor_principal','genero']">> peliculas/admin.py
echo -e "\nfrom django.http import HttpResponse,Http404">> peliculas/views.py
echo -e "\nfrom .models import Pelicula">> peliculas/views.py
echo -e "\ndef home(request):">> peliculas/views.py
echo -e "\tpeliculas=Pelicula.objects.all()">> peliculas/views.py
echo -e "\treturn render(request,'home.html',{'peliculas':peliculas})">> peliculas/views.py
echo -e "\ndef detalles(request,id):">> peliculas/views.py
echo -e "\ttry:pelicula=Pelicula.objects.get(id=id)">> peliculas/views.py
echo -e "\texcept Pelicula.DoesNotExist:raise Http404('No se ha encontrado la pelicula solicitada')">> peliculas/views.py
echo -e "\treturn render(request,'detalles.html',{'pelicula':pelicula})">> peliculas/views.py
mkdir peliculas/templates
