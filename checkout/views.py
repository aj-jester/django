from django.shortcuts import render
from django.http import HttpResponse

from archetypewsgi import Archetype
import json

# Create your views here.

def homePageView(request):
    return HttpResponse("Hello, World!")

def checkoutSessionView(request):
    settings = {
        "app_id": "8adb7f16fcef48668e4aaaab27f3179c",
        "secret_key": "archetype_sk_test_69ac9d65f206493c87faf190b35df056",
    }
    archetype = Archetype(settings=settings)
    tier_id = "prod_M0ivDFxe9xTtvj"
    uid = "ajtest"
    return HttpResponse(json.dumps(archetype.create_checkout_session(uid=uid, tier_id=tier_id)))
