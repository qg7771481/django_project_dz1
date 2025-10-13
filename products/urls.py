from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path(
        "<int:product_pk>/<slug:product_slug>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),


    path('about/', views.about, name='about'),

    path('categories/', views.category_list, name='category_list'),

    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
]