from django.contrib import admin

# Register your models here.
from chat.models import technicalSupportTicket, technicalSuppoertMessages

admin.site.register(technicalSupportTicket)
admin.site.register(technicalSuppoertMessages)
