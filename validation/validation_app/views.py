from django.shortcuts import render, redirect

from validation_app.forms import MyUserForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyUserForm()
    ctx = {
        'form':form
    }
    return render(request, 'validation_app/index.html', ctx)