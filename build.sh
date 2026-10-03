#!/usr/bin/env bash

pip3 install -r requirements.txt

python3 manage.py collectstatic --no-input

python3 manage.py migrate

python3 manage.py shell -c "
from django.contrib.auth.models import User
import os

username = os.environ.get('ADMIN_USERNAME')
password = os.environ.get('ADMIN_PASSWORD')

if username and password:
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print('Admin user created/updated successfully')
"