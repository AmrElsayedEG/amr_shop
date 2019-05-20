from django import forms

from chat.models import technicalSupportTicket, technicalSuppoertMessages


class newTicketForm(forms.ModelForm):
    class Meta:
        model = technicalSupportTicket
        fields = ['title',]

class initialMessageForm(forms.ModelForm):
    class Meta:
        model = technicalSuppoertMessages
        fields = ['message','close_ticket',]
