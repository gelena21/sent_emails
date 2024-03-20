from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from automatic_email import views
from automatic_email.apps import AutomaticEmailConfig

app_name = AutomaticEmailConfig.name

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('client/create/', views.client_create, name='client_create'),
    path('client/<int:client_id>/', views.client_update, name='client_update'),
    path('client/<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('mailout/list/', views.mailout_list, name='mailout_list'),
    path('mailout/create/', views.mailout_create, name='mailout_create'),
    path('mailout/<int:mailout_id>/', views.mailout_update, name='mailout_update'),
    path('mailout/<int:mailout_id>/delete/', views.mailout_delete, name='mailout_delete'),
    path('message/list/', views.message_list, name='message_list'),
    path('message/create/', views.message_create, name='message_create'),
    path('message/<int:message_id>/', views.message_update, name='message_update'),
    path('message/<int:message_id>/delete/', views.message_delete, name='message_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
