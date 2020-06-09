from django.contrib import admin

from employees.models import Company, Employee, Department

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Department)

