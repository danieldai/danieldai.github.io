


https://docs.djangoproject.com/en/1.9/ref/contrib/gis/

https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/

### Install PostGIS

#### Geospatial libraries

```
sudo apt-get install binutils libproj-dev gdal-bin libgeoip1 gdal-bin python-gdal
```

https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/postgis/

```
sudo apt-get install postgis postgresql-server-dev-9.4 python-dev
createuser ming -d -l -r -s -P
createdb linginx
```

https://docs.djangoproject.com/en/1.9/ref/contrib/gis/tutorial/

### Install GeoDjango

```
sudo apt-get install python-pip
sudo pip install virtualenvwrapper
mkdir ~/venvs
```

add following lines to ~/.bashrc, reopen terminal

```
export WORKON_HOME=${HOME}/venvs
. /usr/local/bin/virtualenvwrapper.sh
```

Run following command to create virtualenv

```
mkvirtualenv linginx
```

Adn then install Django

```
pip install Django
pip install psycopg2
```

## Start project

```
django-admin startproject linginx .
cd lingix
./manage.py startapp world
```

### config settings.py

```
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'ming',
         'USER': 'linginx',
     }
}
```

In addition, modify the INSTALLED_APPS setting to include django.contrib.admin, django.contrib.gis, and world (your newly created application):

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'world'
]
```

```
./manage.py makemigrations linginx
./manage.py migrate
```

### install django-extensions

```
pip install django-extensions
```

add it to INSTALLED_APPS

### GDAL Interface



## FAQ

#### What is raster data?

In its simplest form, a **raster** consists of a matrix of cells (or pixels) organized into rows and columns (or a grid) where each cell contains a value representing information, such as temperature. **Rasters** are digital aerial photographs, imagery from satellites, digital pictures, or even scanned maps.

#### What is OGC?

The **OGC** (Open Geospatial Consortium) is an international not for profit organization committed to making quality open standards for the global geospatial community. These standards are made through a consensus process and are freely available for anyone to use to improve sharing of the world's geospatial data.

