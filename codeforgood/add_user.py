import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood.settings')
django.setup()

from django.contrib.auth.models import User
from brake_classroom.models import UserProject

u1 = User.objects.create_user("katya.bacheva", "gmk@gmail.com", "123456")
u1.save()
up1 = UserProject(user=u1)
up1.save()

u2 = User.objects.create_user("georgi.koyrushki", "abv@gmail.com", "123456")
u2.save()
up2 = UserProject(user=u2)
up2.save()

u3 = User.objects.create_user("veselin.vasilev", "gmka@gmail.com", "123456")
u3.save()
up3 = UserProject(user=u3)
up3.save()
