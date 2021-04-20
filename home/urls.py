from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('category/<str:type>', views.category_products, name='category_products'),
]