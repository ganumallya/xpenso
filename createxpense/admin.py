from django.contrib import admin
from .models import TransactionTypes, TransactItems
# Register your models here.

admin.site.register(TransactItems)
admin.site.register(TransactionTypes)