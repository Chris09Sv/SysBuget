from django.shortcuts import render,redirect
from .forms import FacturasForm

# Create your views here.
def factura_create_view(request):
    context = {}
    form =    FacturasForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect('/facturas/create/')
        else:
            form.add_error("user must be logged in")
    context['form'] = form
    return render(request,'facturas/create.html',context)