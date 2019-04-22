from django.contrib import admin

# Register your models here.
from .models import MyModel
from .models import User
from .models import Course

admin.site.register(MyModel)
admin.site.register(User)
admin.site.register(Course)