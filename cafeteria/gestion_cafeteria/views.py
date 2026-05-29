from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt  # Esto permite recibir peticiones POST externas sin problemas de seguridad básicos
def registrar_producto(request):
    if request.method == 'POST':
        cuerpo_peticion = request.body
        datos = json.loads(cuerpo_peticion)
        
        nombre_producto = datos['nombre']
        precio_producto = datos['precio']
        
        # Guardamos en la base de datos usando nuestro modelo
        nuevo_producto = Producto(nombre=nombre_producto, precio=precio_producto)
        nuevo_producto.save()
        
        respuesta = {'mensaje': 'Producto de cafetería creado exitosamente'}
        return JsonResponse(respuesta)