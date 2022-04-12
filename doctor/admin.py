from django.contrib import admin
from doctor.models.doctor import Doctor
from doctor.models.customer import Customer
from medicine.models.storage import Storage
from medicine.models.income import Income

admin.site.site_header = '医院管理后台'
admin.site.site_title = '医院管理后台'
admin.site.index_title = '医院管理后台'


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'sector')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'phone')


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'datetime', 'exp')


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('sum', 'type', 'datatime', 'purpose', 'remark')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Income, IncomeAdmin)
