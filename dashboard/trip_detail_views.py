import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


API_BASE = settings.BUS_API_BASE


def _auth_headers(request):
    token = request.session.get("bs_token", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept":        "application/json",
        "Content-Type":  "application/json",
    }


# =========================================================
# PAGE VIEW  — renders the detail page for one trip
# =========================================================

def trip_detail_page(request, trip_id):
    return render(request, "dashboard/trip_detail.html", {"trip_id": trip_id})


# =========================================================
# GET TRIP SEATS  (new dedicated endpoint)
# =========================================================

@require_http_methods(["GET"])
def get_trip_seats(request, trip_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetTripSeatsOfTripInstance?tripInstanceId={trip_id}",
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
# GET TRIP INSTANCE DETAIL
# =========================================================

@require_http_methods(["GET"])
def get_trip_detail(request, trip_id):
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
# GET ALL DRIVERS  (employees filtered to driver type)
# =========================================================

@require_http_methods(["GET"])
def get_drivers(request):
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
        # Filter only drivers on the Django side
        if data.get("result"):
            drivers = [
                e for e in data["result"]
                if (e.get("busCompanyEmployeeTypeName") or "").lower() == "driver"
            ]
            data["result"] = drivers
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# ASSIGN DRIVER
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def assign_driver(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "tripInstanceId": body.get("tripInstanceId"),
            "driverId":       body.get("driverId"),
        }
        response = requests.post(
            f"{API_BASE}/AssignDriver",
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
