from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto
from django.core import serializers
import json
import django
# Create your views here.

def obtener_token(request):
    token = django.middleware.csrf.get_token(request)
    print(token)
    return HttpResponse(json.dumps(token))


def busqueda(request):
    if request.method == "POST":
        request.POST = request.body.decode('utf-8')
        request.POST = json.loads(request.POST)
        producto = request.POST["text_producto"]
        articles = Articulos.objects.filter(nombre_articulo__icontains=producto)
        articles = serializers.serialize('json', list(articles), fields=('nombre_articulo','seccion','precio'))

        return HttpResponse({articles}, content_type="application/json")
    message = "Hola, este mensaje viene del backend, busca un producto :D"
    return HttpResponse(json.dumps(message), content_type="application/json")


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
        message = "Muchas gracias por usarme! :D"
        response = {
            "message": message,
            "data": send_mail
        }
        return HttpResponse(json.dumps(response), content_type="application/json")
    message = "Hola, este mensaje viene del backend :D"
    return HttpResponse(json.dumps(message), content_type="application/json")


# Contactar con API FORMS
def contactar1(request):
    if request.method == "POST":

        my_form = FormularioContacto(request.POST)

        if my_form.is_valid():
            data_form = my_form.cleaned_data
            asunto = data_form["asunto"]
            mensaje = data_form["mensaje"]
            email = data_form["email"]
            send_mail = (asunto, mensaje, email)
            message = "Muchas gracias por usarme, soy un Custom Form! :D"

            response = {
                "message": message,
                "data": send_mail
            }
            return HttpResponse(json.dumps(response), content_type="application/json")
        return HttpResponse({'Algo salió mal en la petición :('}, content_type="application/json")

    else:
        message = "Hola, este mensaje viene del backend, estás usando un Custom Form :D"
        new_form = FormularioContacto()
        response = {
                "message": message,
                "new_form": new_form
            }
        return HttpResponse(json.dumps(message), content_type="application/json", )
