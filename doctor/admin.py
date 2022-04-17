from django.contrib import admin
from doctor.models.doctor import Doctor
from doctor.models.customer import Customer
from doctor.models.pet import Pet
from medicine.models.storage import Storage
from medicine.models.income import Income
from doctor.models.register import Register
from doctor.models.prescription import Prescription
from doctor.models.booking import Booking

admin.site.site_header = '医院管理后台'
admin.site.site_title = '医院管理后台'
admin.site.index_title = '医院管理后台'


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'phone', 'sector')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'phone')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('time', 'customer', 'exp')


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'customer')


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'datetime', 'exp')


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('sum', 'type', 'datatime', 'purpose', 'remark')


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'time', 'price', 'customer')


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'time', 'content', 'customer')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Booking, BookingAdmin)
