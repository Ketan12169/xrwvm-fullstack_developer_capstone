from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class

# CarModelAdmin class
# @admin.register(CarMake)
# class CarMakeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description')
#     search_fields = ('name',)

# @admin.register(CarModel)
# class CarModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'car_make', 'type', 'year')
#     list_filter = ('car_make', 'type')
#     search_fields = ('name',)

# CarMakeAdmin class with CarModelInline

# Register models here
