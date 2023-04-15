from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

### Nueva clase que hereda de Model Admin
### Se usa para personalizar la mostrada de datos en el panel
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre_cliente", "direccion", "email")
    search_fields=("nombre_cliente","email")


##Nueva clase
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

# Register your models here.
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos)