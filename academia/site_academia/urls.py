from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('plano/', views.plano_view, name='plano'),
    path('treinadores/', views.Treinadores_view, name='treinadores'),
    path('contato/', views.contato, name='contato'),
    path('cadastrar_cliente/', views.cadastro_cliente, name='cadastrar_cliente'),
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(), name='alterar-senha'),
    path('senha-alterada/', auth_views.PasswordChangeDoneView.as_view(), name='senha-alterada'),
    path('senha/esqueceu/', auth_views.PasswordResetView.as_view(), name='esqueceu-senha'),
    path('senha/redefinir/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='redefinir-senha'),
    path('senha-redefinida/', auth_views.PasswordResetCompleteView.as_view(), name='senha-redefinida'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Adicionando a URL de login
    path('logout/', views.user_logout, name='logout'),  # Adicionando a URL de logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
