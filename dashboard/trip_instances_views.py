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

def trip_instances_page(request):
    return render(request, "dashboard/trip_instances.html")


# =========================================================
# GET ALL TRIP INSTANCES
# =========================================================

@require_http_methods(["GET"])
def get_trip_instances(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllTripInstances",
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
# GET SINGLE TRIP INSTANCE
# =========================================================

@require_http_methods(["GET"])
def get_trip_instance(request, trip_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetTripInstance/{trip_id}",
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
# GET ALL TRIP SCHEDULES  (for filter dropdown)
# =========================================================

@require_http_methods(["GET"])
def get_schedules_for_instances(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllTripSchedules",
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
# GET ALL BUS COMPANIES  (for filter dropdown)
# =========================================================

@require_http_methods(["GET"])
def get_companies_for_instances(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBusCompanies",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
