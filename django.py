pip3 install django
django-admin.py startproject cineteca && cd cineteca
python manage.py startapp peliculas

x=django.contrib.admin;sed -i "/$x/s/^\(\s\+\)'"$x"',/\1'peliculas',\n\1'"$x"',/" cineteca/settings.py
sed -i "/^from.*path/s/$/,re_path/" cineteca/urls.py
sed -i "/^from django.urls/afrom peliculas import views" cineteca/urls.py
sed -i "/admin.site.urls/s/^\(\s\+\)\(path.*$\)/\1\2\n\1path('',views.home,name='home'),/" cineteca/urls.py
sed -i "/admin.site.urls/s/^\(\s\+\)\(path.*$\)/\1\2\n\1re_path('peliculas\/(\\\d+)',views.detalles,name='detalles'),/" cineteca/urls.py
echo -e "\nclass Pelicula(models.Model):">> peliculas/models.py
echo -e "\ttitulo=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tdirector=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tactor_principal=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tactriz_principal=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tgenero=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tpais=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tfecha_estreno=models.IntegerField()">> peliculas/models.py
echo -e "\tpremios=models.ManyToManyField('Premio',blank=True)">> peliculas/models.py
echo -e "\nclass Premio(models.Model):">> peliculas/models.py
echo -e "\tpremio=models.CharField(max_length=90)">> peliculas/models.py
echo -e "\tdef __str__(self):return self.premio">> peliculas/models.py
echo -e "\nfrom .models import Pelicula">> peliculas/admin.py
echo -e "\n@admin.register(Pelicula)">> peliculas/admin.py
echo -e "class PeliculaAdmin(admin.ModelAdmin):">> peliculas/admin.py
echo -e "\tlist_display=['titulo','director','actor_principal','actriz_principal','genero']">> peliculas/admin.py
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
cp ../*html peliculas/templates/
mkdir -p peliculas/management/commands
cp ../cargar_CSV.py peliculas/management/commands/

python manage.py makemigrations
python manage.py migrate
python manage.py cargar_CSV

python manage.py runserver 0.0.0.0:8080 2>&1 1>/dev/null&

python manage.py createsuperuser

