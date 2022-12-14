import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def hello(request):
    return JsonResponse({"status": "ok"})

# Функция работает корректно
# def index(request):
#     if request.method == "GET":
#         categories = Category.objects.all()
#         response = []
#         for category in categories:
#             response.append({"id": category.id,
#                              "name": category.name
#                              })
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        category_search = request.GET.get("name", None)
        response = []

        if category_search:
            categories = categories.filter(name=category_search)
            for category in categories:
                response.append({"id": category.id,
                                 "name": category.name
                                 })
            return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

        elif category_search is None:
            for category in categories:
                response.append({"id": category.id,
                                 "name": category.name
                                 })
            return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        category_data = json.loads(request.body)
        category = Category()
        category.name = category_data["name"]

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
            })


class CategoryDetailView(DetailView):
    # Работает
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.id,
                             "name": category.name
                             })


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        ad_search = request.GET.get("author", None)
        response = []

        if ad_search:
            ads = ads.filter(author=ad_search)
            for ad in ads:
                response.append({"id": ad.id,
                                 "name": ad.name,
                                 "author": ad.author,
                                 "price": ad.price,
                                 "description": ad.description,
                                 "address": ad.address,
                                 "is_published": ad.is_published,
                                 })
            return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

        elif ad_search is None:
            for ad in ads:
                response.append({"id": ad.id,
                                 "name": ad.name,
                                 "author": ad.author,
                                 "price": ad.price,
                                 "description": ad.description,
                                 "address": ad.address,
                                 "is_published": ad.is_published,
                                 })
            return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ad()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]

        ad.save()

        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             "description": ad.description,
                             "address": ad.address,
                             "is_published": ad.is_published,
                             })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             "description": ad.description,
                             "address": ad.address,
                             "is_published": ad.is_published,
                             })

