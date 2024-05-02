from django.shortcuts import render
from .models import User
from .forms import userForm
import subprocess


def homepage(request):

    users =  User.objects.all()
    form = userForm()
    if request.method =="POST" :
        form=userForm(request.POST)
        if form.is_valid():

            if not form.cleaned_data['hidden'] :
                form.save()
            else:
                title = "ALERT"
                message = "You are Under attack"
                subprocess.Popen(['notify-send', title, message])

        else:
            print(form.errors)
    context ={'list':users,'form':form}
    return render(request,'base.html',context=context)