from django.urls import path, include
from . import views


app_name = 'order'
urlpatterns = [
    path('thank-you/<int:unique_order_id>/', views.thank_you, name='thanks')
    ]
