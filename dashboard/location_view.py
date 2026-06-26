import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# =========================================================
# CONFIG
# =========================================================

API_BASE = settings.BUS_API_BASE

def _auth_headers(request):
    token = request.session.get("bs_token", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept":        "application/json",
        "Content-Type":  "application/json",
    }

# =========================================================
# PAGE VIEW
# =========================================================

def locations_page(request):
    return render(request, "dashboard/location.html")


# =========================================================
# GET GOVERNORATES
# =========================================================

@require_http_methods(["GET"])
def get_governorates(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllGovernorates",
            headers=_auth_headers(request),
            timeout=30
        )

        data = response.json()

        return JsonResponse(data, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return JsonResponse({
            "error": str(e),
            "hasErrors": True
        }, status=500)

    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "hasErrors": True
        }, status=500)


# =========================================================
# GET CITIES
# =========================================================

@require_http_methods(["GET"])
def get_cities(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllCities",
            headers=_auth_headers(request),
            timeout=30
        )

        data = response.json()

        return JsonResponse(data, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return JsonResponse({
            "error": str(e),
            "hasErrors": True
        }, status=500)

    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "hasErrors": True
        }, status=500)


# =========================================================
# CREATE CITY
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def create_city(request):
    try:
        body = json.loads(request.body.decode("utf-8"))

        payload = {
            "nameAr": body.get("nameAr"),
            "nameEn": body.get("nameEn"),
            "governorateId": body.get("governorateId"),
        }

        json_payload = json.dumps(payload, ensure_ascii=False)

        response = requests.post(
            f"{API_BASE}/CreateCity",
            data=json_payload, 
            headers=_auth_headers(request),
            timeout=30
        )


        try:
            data = response.json()
        except Exception:
            data = {
                "error": "Invalid JSON response",
                "raw": response.text
            }

        return JsonResponse(data, status=response.status_code)

    except json.JSONDecodeError:
        return JsonResponse({
            "error": "Invalid JSON body",
            "hasErrors": True
        }, status=400)

    except Exception as e:
        return JsonResponse({
            "error": str(e),
            "hasErrors": True
        }, status=500)

# =========================================================
# UPDATE CITY
# =========================================================

import json

@csrf_exempt
@require_http_methods(["POST"])
def update_city(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))

        payload = {
            "id": body.get("id"),
            "nameAr": body.get("nameAr"),
            "nameEn": body.get("nameEn"),
            "governorateId": body.get("governorateId"),
        }

        json_payload = json.dumps(payload, ensure_ascii=False)

        response = requests.post(
            f"{API_BASE}/UpdateCity",
            data=json_payload,
            headers=_auth_headers(request),
            timeout=30
        )

        return JsonResponse(response.json(), safe=False, status=response.status_code)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)