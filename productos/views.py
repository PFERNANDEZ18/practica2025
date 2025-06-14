from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos

def index_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/index_productos.html',{'productos':productos})

def registrar_productos(request):
    if request.method=='POST':
        cod = request.POST.get('cod')
        nombre = request.POST.get('nombre')
        description = request.POST.get('description')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        Productos.objects.create(
            cod=cod,
            nombre=nombre,
            description=description,
            precio=precio,
            stock=stock
        )

        return redirect('index_productos')
    return render(request,'productos/registrar_productos.html')

def editar_productos(request, producto_id):
    productos = get_object_or_404(Productos, id=producto_id)

    if request.method =='POST':
        productos.cod = request.POST.get('cod')
        productos.nombre = request.POST.get('nombre')
        productos.description = request.POST.get('description')
        productos.precio = request.POST.get('precio')
        productos.stock = request.POST.get('stock')
        productos.save()
        return redirect('index_productos')
    return render(request, 'productos/editar_productos.html', {'productos':productos})

def eliminar_productos(request, id):
    if request.method == 'POST':
        productos = Productos.objects.get(pk=id)
        productos.delete()
        return JsonResponse({'success':True})