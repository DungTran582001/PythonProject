from django.contrib import admin

from .models import Expense,Income,Member
# Register your models here.

admin.site.register(Member)
admin.site.register(Expense)
admin.site.register(Income)
