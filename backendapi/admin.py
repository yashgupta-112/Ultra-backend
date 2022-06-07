from django.contrib import admin
from .models import plans,info,tickets,service,addon
# Register your models here.

# Register your models here.
admin.site.register(plans)
admin.site.register(info)
admin.site.register(tickets)
admin.site.register(addon)
admin.site.register(service)