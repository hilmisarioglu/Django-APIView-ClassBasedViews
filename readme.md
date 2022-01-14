# CRUD
```bash
# CREATING VIRTUAL ENVIRONMENT

# windows
py -m venv env
# windows other option
python -m venv env

# ACTIVATING ENVIRONMENT
# windows
source ./env/Scripts/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
django-admin --version
django-admin startproject main .
```

go to settings.py, make amendments below
```python
from decouple import config
SECRET_KEY = config('SECRET_KEY')
go to terminal
```bash
py manage.py migrate
py manage.py runserver
```
click the link with CTRL key pressed in the terminal and see django rocket.
go to terminal, stop project, add app
```
py manage.py startapp fscohort
```
go to settings.py and add 'fscohort' app to installed apps and add below lines
```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
create these folders at project level as /media/student
go to fscohort/models.py

```python
from django.db import models
# Create your models here.
class Kayit(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="kayit/", default="avatar.png")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```
go to terminal
```bash
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate
```
