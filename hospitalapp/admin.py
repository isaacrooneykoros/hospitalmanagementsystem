from django.contrib import admin
from hospitalapp.models import User, product, Member, Contact

# Register your models here.
admin.site.register(User)
admin.site.register(product)
admin.site.register(Member)
admin.site.register(Contact)
