from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from controller import generate_api


app = NinjaAPI()
generate_api(app)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.urls),

]
