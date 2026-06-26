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

def trip_schedules_page(request):
    return render(request, "dashboard/trip_schedules.html")


# =========================================================
# GET ALL TRIP SCHEDULES
# =========================================================

@require_http_methods(["GET"])
def get_trip_schedules(request):
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
# GET SINGLE TRIP SCHEDULE
# =========================================================

@require_http_methods(["GET"])
def get_trip_schedule(request, trip_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetTripSchedule/{trip_id}",
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
# CREATE TRIP SCHEDULE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def create_trip_schedule(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "busRouteId":    body.get("busRouteId"),
            "departureTime": body.get("departureTime"),
            "arrivalTime":   body.get("arrivalTime"),
            "price":         body.get("price"),
            "activeDays":    body.get("activeDays", []),
            "defaultBusId":  body.get("defaultBusId"),
        }
        response = requests.post(
            f"{API_BASE}/CreateTripSchedule",
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
# UPDATE TRIP SCHEDULE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def update_trip_schedule(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "id":            body.get("id"),
            "departureTime": body.get("departureTime"),
            "arrivalTime":   body.get("arrivalTime"),
            "price":         body.get("price"),
            "activeDays":    body.get("activeDays", []),
            "defaultBusId":  body.get("defaultBusId"),
        }
        response = requests.post(
            f"{API_BASE}/UpdateTripSchedule",
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
# DELETE TRIP SCHEDULE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def delete_trip_schedule(request, trip_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.post(
            f"{API_BASE}/DeleteTripSchedule/{trip_id}",
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
# GET ALL ROUTES  (for route dropdown in create form)
# =========================================================

@require_http_methods(["GET"])
def get_routes_for_trips(request):
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
# GET ALL BUSES  (for defaultBusId dropdown)
# =========================================================

@require_http_methods(["GET"])
def get_buses_for_trips(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBuses",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


@require_http_methods(["GET"])
def get_drivers_for_schedules(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBusCompanyEmployees",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        if data.get("result"):
            data["result"] = [
                e for e in data["result"]
                if (e.get("busCompanyEmployeeTypeName") or "").lower() == "driver"
            ]
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)