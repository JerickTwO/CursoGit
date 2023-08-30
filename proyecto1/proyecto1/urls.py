
from django.contrib import admin
from django.urls import path
from proyecto1.views import saludo,dame_fecha,despedida,calcula_edad,curso_c,curso_css
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', saludo),
    path('nosveremos/', despedida),
    path('edades/<int:edad>/<int:anio>',calcula_edad),
    path('fecha/',dame_fecha),
    path('curso_c/',curso_c),
    path('curso_css/',curso_css),
]
