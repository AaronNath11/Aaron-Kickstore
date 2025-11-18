from django.urls import path
from main import views
from main.views import show_main, create_product, show_product, delete_product, show_xml, show_json, show_xml_by_id, show_json_by_id, proxy_image, create_product_flutter, get_user
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import add_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('create/', create_product, name='create_product'),
    path('detail/<uuid:id>/', show_product, name='show_product'),
    path("delete/<uuid:id>/", delete_product, name="delete_product"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path("get_user/", get_user, name="get_user"),

] 
