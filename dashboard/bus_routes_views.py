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

def routes_page(request):
    return render(request, "dashboard/bus_routes.html")


# =========================================================
# GET ALL ROUTES
# =========================================================

@require_http_methods(["GET"])
def get_routes(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBusRoutes",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()

        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# GET SINGLE ROUTE
# =========================================================

@require_http_methods(["GET"])
def get_route(request, route_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetBusRoute/{route_id}",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# CREATE ROUTE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def create_route(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "busCompanyOfficeId": body.get("busCompanyOfficeId"),
            "fromCityId":         body.get("fromCityId"),
            "toCityId":           body.get("toCityId"),
        }
        response = requests.post(
            f"{API_BASE}/CreateBusRoute",
            data=json.dumps(payload, ensure_ascii=False),
            headers=_auth_headers(request),
            timeout=30,
        )
        try:
            data = response.json()
        except Exception:
            data = {"error": "Invalid JSON response", "raw": response.text}
        return JsonResponse(data, status=response.status_code)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body", "hasErrors": True}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# UPDATE ROUTE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def update_route(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "id":         body.get("id"),
            "fromCityId": body.get("fromCityId"),
            "toCityId":   body.get("toCityId"),
        }
        response = requests.post(
            f"{API_BASE}/UpdateBusRoute",
            data=json.dumps(payload, ensure_ascii=False),
            headers=_auth_headers(request),
            timeout=30,
        )
        try:
            data = response.json()
        except Exception:
            data = {"error": "Invalid JSON response", "raw": response.text}
        return JsonResponse(data, status=response.status_code)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body", "hasErrors": True}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# DELETE ROUTE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def delete_route(request, route_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.post(
            f"{API_BASE}/DeleteBusRoute/{route_id}",
            headers=_auth_headers(request),
            timeout=30,
        )
        try:
            data = response.json()
        except Exception:
            data = {"hasErrors": False}
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# GET ALL CITIES
# =========================================================

@require_http_methods(["GET"])
def get_cities_for_routes(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllCities",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# GET ALL OFFICES
# =========================================================

@require_http_methods(["GET"])
def get_offices_for_routes(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBusCompanyOffices",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)