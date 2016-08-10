from django.contrib import admin
from .models import People_model
from .models import Activity_model,detail_model
admin.site.register(People_model)
admin.site.register(Activity_model)
admin.site.register(detail_model)
