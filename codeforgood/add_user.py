import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood.settings')
django.setup()

from django.contrib.auth.models import User

u1 = User.objects.create_user("user_a", "abv@abv.bg", "123456")
u1.save()

u2 = User.objects.create_user("user_b", "gmk@gmail.com", "123456")
u2.save()

u3 = User.objects.create_user("user_c", "gmail@gmail.com", "123456")
u3.save()