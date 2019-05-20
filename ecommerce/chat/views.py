from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from chat.forms import newTicketForm, initialMessageForm
from chat.models import technicalSupportTicket, technicalSuppoertMessages


def startTicket(request):
    tickets = technicalSupportTicket.objects.filter(user=request.user)
    context = {'tickets':tickets}
    return render(request, 'tickets.html', context)

def newTicket(request):
    if request.method == 'POST':
        ticketForm = newTicketForm(request.POST)
        if ticketForm.is_valid():
            m = technicalSupportTicket()
            m.user = request.user
            m.title = ticketForm.cleaned_data['title']
            m.save()
    else:
        ticketForm = newTicketForm
    context = {
        'ticketForm':ticketForm,
               }
    return render(request,'new_ticket.html',context)

def message(request,id):
    user = User.objects.get(id=1)
    tic = technicalSupportTicket.objects.get(id=id)
    if not request.user.is_superuser:
        if tic.user == request.user:
            error = False
            allM = technicalSuppoertMessages.objects.filter(ticket=tic)
            if request.method == 'POST':
                message_form = initialMessageForm(request.POST)
                if message_form.is_valid():
                    m = technicalSuppoertMessages()
                    m.ticket = tic
                    m.one = request.user
                    m.two = user
                    m.message = message_form.cleaned_data['message']
                    m.close = message_form.cleaned_data['close_ticket']
                    m.save()
                    if m.close:
                        update_close = technicalSupportTicket.objects.get(id=id)
                        update_close.is_open = 'False'
                        update_close.save()
                    else:
                        update_close = technicalSupportTicket.objects.get(id=id)
                        update_close.is_open = 'True'
                        update_close.save()

            else:
                message_form = initialMessageForm
        else:
            error = 'No Ticket ID for this user'
            allM = None
            message_form = initialMessageForm
    else:
        error = False
        allM = technicalSuppoertMessages.objects.filter(ticket=tic)
        if request.method == 'POST':
            message_form = initialMessageForm(request.POST)
            if message_form.is_valid():
                m = technicalSuppoertMessages()
                m.ticket = tic
                m.one = user
                m.two = user
                m.message = message_form.cleaned_data['message']
                m.close = message_form.cleaned_data['close_ticket']
                m.save()
                if m.close:
                    update_close = technicalSupportTicket.objects.get(id=id)
                    update_close.is_open = 'False'
                    update_close.save()
                else:
                    update_close = technicalSupportTicket.objects.get(id=id)
                    update_close.is_open = 'True'
                    update_close.save()
            else:
                message_form = initialMessageForm
        else:
            allM = None
            message_form = initialMessageForm
    context = {
        'all':allM,
        'id':id,
        'tic':tic.is_open,
        'message_form':message_form,
        'error':error
    }
    return render(request,'chat.html',context)

def supportAdminAll(request):
    if request.user.is_superuser:
        opened = technicalSupportTicket.objects.filter(is_open='True')
        closed = technicalSupportTicket.objects.filter(is_open='False')
    else:
        opened = None
        closed = None
    context = {
        'opened':opened,
        'closed':closed
    }
    return render(request,'tickets_admin.html',context)