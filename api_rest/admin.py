from django.contrib import admin
from .models import User, Contact, Message, ContactKanban

# Register your models here.
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(ContactKanban)