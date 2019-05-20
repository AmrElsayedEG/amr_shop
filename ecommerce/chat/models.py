from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class technicalSupportTicket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='admin' ,related_name='user') #from < when user send >
    #to = models.ForeignKey(User, on_delete=models.CASCADE, default=str('admin'), related_name='to')   #to   < when admin send >
    title = models.CharField(max_length=150)
    is_open = models.CharField(max_length=5,default='True')
    def __str__(self):
        return self.title

class technicalSuppoertMessages(models.Model):
    ticket = models.ForeignKey(technicalSupportTicket,on_delete=models.CASCADE)
    one = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='one')
    two = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='two')
    message = models.CharField(max_length=500)
    close_ticket = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ticket)
