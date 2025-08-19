from django.contrib import admin
from .Model.Contact import Contact
from .Model.Message import Message
from .Model.KanbanContact import ContactKanban
from .Model.Profile import Profile
from .Model.Enterprise import Enterprise
from .Model.SessionWhatsapp import SessionWhatsApp
from .Model.WhatsappVariables import WhatsappVariables


# Register your models here.
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(ContactKanban)
admin.site.register(Profile)
admin.site.register(Enterprise)
admin.site.register(SessionWhatsApp)
admin.site.register(WhatsappVariables)