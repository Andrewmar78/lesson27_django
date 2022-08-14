import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from app.models import Category, Ads


def hello(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        search_text = request.GET.get("Котики", None)
        if search_text:
            response = []
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

        return JsonResponse({"id": category.id,
                             "name": category.name,
                             })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.id,
                             "name": category.name
                             })


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        ads = Ads.objects.all()
        search_text = request.GET.get("котята", None)
        if search_text:
            response = []
            for ad in ads:
                response.append({"id": ads.id,
                                 "name": ads.name,
                                 "author": ads.author,
                                 "price": ads.price,
                                 "description": ads.description,
                                 "address": ads.address,
                                 "is_published": ads.is_published,
                                 })
            return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ads()
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
    model = Ads

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
