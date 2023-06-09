from django.shortcuts import render,redirect
from .forms import ClientesForm

# Create your views here.
def cliente_create_view(request):
    context ={}
    form = ClientesForm(request.POST or None)
   
    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect('/clientes/create/')
        else:
            form.add_error("user must be logged in")
    context['form'] = form
    return render(request,'clientes/create.html',context)
