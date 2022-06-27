from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blogger import views

app_name='blogger'

urlpatterns = [
    path("crear_usuario/", views.SignUpView.as_view(), name ="blogger_signup"),
    path("perfil_usuario/<int:pk>", views.BloggerProfile.as_view(), name ="blogger_profile"),
    path("editar_usuario/<int:pk>", views.BloggerUpdate.as_view(), name ="blogger_edit"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)