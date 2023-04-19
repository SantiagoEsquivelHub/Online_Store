from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto
import json
# Create your views here.


def buscar_productos(request):
    return render(request, "buscar_productos.html")
    # return render(request, "/home/oswaldo/djangoProject/TiendaOnline/gestionPedidos/templates/buscar_productos.html")


def procesar_busqueda(request):
    mensaje = "Articulo: %r" % request.GET["text_producto"]
    producto = request.GET["text_producto"]
    articulos = Articulos.objects.filter(nombre_articulo__icontains=producto)

    return render(request, "resultados_busqueda.html",
                  {"articulos": articulos, "query": producto})

    # return HttpResponse(mensaje)


def contactar(request):
    if request.method == "POST":
        request.POST = request.body.decode('utf-8')
        request.POST = json.loads(request.POST)

        subject = request.POST.get("text_asunto", "")
        email_message = request.POST.get("area_mensaje", "") + \
            " " + request.POST.get("text_email", "")
        email_user = settings.EMAIL_HOST_USER
        recipient_list = "cuenta@gmail.com"
        send_mail = (subject, email_message, email_user, recipient_list)
        response = {
            "message": "Muchas gracias por usarme! :D",
            "data": send_mail
        }
        return HttpResponse(json.dumps(response), content_type="application/json")

        #  return render(request, "gracias.html")
    return HttpResponse({"Hello there! This message is sent from the backend :D"})

    # return render(request, "contactar.html")

# Contactar con API FORMS


def contactar1(request):
    if request.method == "POST":
        my_form = FormularioContacto(request.POST)
        if my_form.is_valid():
            data_form = my_form.cleaned_data
            subject = data_form["text_asunto"]
            # send_mail()
            return render(request="gracias.html")

    else:
        new_form1 = FormularioContacto()

    return render(request, "contactar1.html", {"form": new_form1})
