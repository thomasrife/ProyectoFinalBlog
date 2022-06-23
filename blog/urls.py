from django.urls import path
# Vista Home
from .views import BlogCreate, BlogDelete, BlogList, BlogUpdate, Home


app_name='blog'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('listar_posts/', BlogList.as_view(), name='blog_list'),
    path('crear_post/', BlogCreate.as_view(), name='blog_create'),
    path('editar_post/<int:pk>', BlogUpdate.as_view(), name='blog_update'),
    path('eliminar_post/<int:pk>', BlogDelete.as_view(), name='blog_delete')
    
]