from django.contrib import admin

# Register your models here.
from .models import MyModel
from .models import User

admin.site.register(MyModel)
admin.site.register(User)