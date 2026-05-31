from django.http import JsonResponse
from .models import Producto, Venta
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def registrar_producto(request):
    
    # Lógica para GUARDAR un producto nuevo
    if request.method == 'POST':
        cuerpo_peticion = request.body
        datos = json.loads(cuerpo_peticion)
        
        nombre_producto = datos['nombre']
        precio_producto = datos['precio']
        
        nuevo_producto = Producto(nombre=nombre_producto, precio=precio_producto)
        nuevo_producto.save()
        
        respuesta = {'mensaje': 'Producto de cafetería creado exitosamente'}
        return JsonResponse(respuesta)

    # Lógica para CONSULTAR los productos guardados
    elif request.method == 'GET':
        # 1. Obtenemos todos los registros de la base de datos
        productos_guardados = Producto.objects.all()
        
        # 2. Creamos una lista vacía para almacenar los datos
        lista_productos = []
        
        # 3. Iteramos de forma explícita sobre cada producto
        for producto in productos_guardados:
            diccionario_producto = {
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio) # Convertimos el decimal a texto para el JSON
            }
            lista_productos.append(diccionario_producto)
            
        # 4. Retornamos la lista completa en formato JSON
        return JsonResponse({'menu': lista_productos})
    
@csrf_exempt
def registrar_venta(request):
    if request.method == 'POST':
        cuerpo_peticion = request.body
        datos = json.loads(cuerpo_peticion)
        
        # Esperamos recibir una lista de IDs, por ejemplo: {"productos_ids": [1, 2, 1]}
        lista_ids = datos['productos_ids']
        
        total_venta = 0
        
        # Iteramos explícitamente sobre cada ID para buscar su precio y sumarlo
        for id_producto in lista_ids:
            # Buscamos el producto en la base de datos por su ID
            producto_db = Producto.objects.get(id=id_producto)
            total_venta = total_venta + producto_db.precio
            
        # Guardamos el registro de la venta con el total calculado
        nueva_venta = Venta(total=total_venta)
        nueva_venta.save()
        
        respuesta = {
            'mensaje': 'Venta registrada exitosamente',
            'total_cobrado': str(total_venta)
        }
        return JsonResponse(respuesta)