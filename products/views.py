from django.http.request import HttpRequest
from django.http.response import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from .models import Product, Category, Brand


def product_list(request: HttpRequest) -> HttpResponse:
    """Функція обробника вхідного запиту на отримання списку товарів."""
    products = Product.objects.all()
    return render(request, "products/product_list.html", context={"products": products})


def product_detail(
    request: HttpRequest, product_pk: int, product_slug: str
) -> HttpResponse:
    """Функція обробника вхідного запиту на отримання одного товару з pk та slug."""
    product = Product.objects.filter(pk=product_pk, slug=product_slug).first()
    if product is None:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    if not product.available:
        return HttpResponseForbidden("<h1>Forbidden</h1>")

    return render(
        request,
        template_name="products/product_detail.html",
        context={"product": product},
    )


class IndexPageView(TemplateView):
    template_name = "index_page.html"


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    model = Product
    # {"product_pk": 5, "product_slug": "samsung"}
    pk_url_kwarg = "product_pk"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"


class BrandDetailView(DetailView):
    template_name = "products/brand_detail.html"
    model = Brand
    pk_url_kwarg = "pk"
    context_object_name = "brand"


class BrandListView(ListView):
    template_name = "products/brand_list.html"
    model = Brand
    pk_url_kwarg = "pk"
    context_object_name = "brands"

def about(request):
    """
    View-функція для відображення сторінки "Про нас".
    """
    return render(request, 'products/about.html')


def category_list(request):
    """Відображення списку всіх категорій."""
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_detail(request, category_slug):
    """Відображення товарів конкретної категорії."""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, availability=True)
    return render(request, 'products/category_detail.html', {'category': category, 'products': products})