from django.contrib import admin 
from .models import Person, Reservations, Employee
from django.contrib.auth.admin import UserAdmin
# Register your models here.  
from django.contrib.auth.models import User 
# Unregister the provided model admin:  
admin.site.unregister(User) 
admin.site.register(Reservations)
admin.site.register(Employee)


@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form
    

@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", )