from django.contrib import admin

# Register your models here.
from .models import MyModel
from .models import User
from .models import Course
from .models import Lab

admin.site.register(MyModel)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lab)