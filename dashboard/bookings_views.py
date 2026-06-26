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

def bookings_page(request):
    return render(request, "dashboard/bookings.html")


# =========================================================
# GET ALL BOOKINGS
# =========================================================

@require_http_methods(["GET"])
def get_bookings(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBookings",
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
# GET SINGLE BOOKING
# =========================================================

@require_http_methods(["GET"])
def get_booking(request, booking_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetBooking/{booking_id}",
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
# GET BOOKINGS BY TRIP INSTANCE
# =========================================================

@require_http_methods(["GET"])
def get_bookings_by_trip(request, trip_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetBookingsByTripInstance/{trip_id}",
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
# CREATE BOOKING
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def create_booking(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "tripInstanceId": body.get("tripInstanceId"),
            "seats":          body.get("seats", []),
        }
        response = requests.post(
            f"{API_BASE}/CreateBooking",
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
# UPDATE BOOKING
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def update_booking(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "id":       body.get("id"),
            "statusId": body.get("statusId"),
            "seats":    body.get("seats", []),
        }
        response = requests.post(
            f"{API_BASE}/UpdateBooking",
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
# CANCEL BOOKING
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def cancel_booking(request, booking_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.post(
            f"{API_BASE}/CancelBooking/{booking_id}",
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
# GET ALL TRIP INSTANCES  (for create booking dropdown)
# =========================================================

@require_http_methods(["GET"])
def get_trips_for_bookings(request):
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


@require_http_methods(["GET"])
def get_trip_instance_for_booking(request, trip_id):
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
        print(f"data is {data}")
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)