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


# ── Page ──────────────────────────────────────────────
def payments_page(request):
    return render(request, "dashboard/payments.html")


# ── GET ALL PAYMENTS ───────────────────────────────────
@require_http_methods(["GET"])
def get_payments(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(f"{API_BASE}/GetAllPayments", headers=_auth_headers(request), timeout=30)
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# ── GET PAYMENT METHODS ────────────────────────────────
@require_http_methods(["GET"])
def get_payment_methods(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(f"{API_BASE}/GetPaymentMethods", headers=_auth_headers(request), timeout=30)
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# ── GET PAYMENT STATUSES ───────────────────────────────
@require_http_methods(["GET"])
def get_payment_statuses(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(f"{API_BASE}/GetPaymentStatuses", headers=_auth_headers(request), timeout=30)
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# ── GET ALL BOOKINGS (for booking dropdown in create) ──
@require_http_methods(["GET"])
def get_bookings_for_payments(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(f"{API_BASE}/GetAllBookings", headers=_auth_headers(request), timeout=30)
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# ── CREATE PAYMENT ─────────────────────────────────────
@csrf_exempt
@require_http_methods(["POST"])
def create_payment(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "bookingId":       body.get("bookingId"),
            "paymentMethodId": body.get("paymentMethodId"),
        }
        response = requests.post(
            f"{API_BASE}/CreateCashPayment",
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


# ── UPDATE PAYMENT ─────────────────────────────────────
@csrf_exempt
@require_http_methods(["POST"])
def update_payment(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))
        payload = {
            "id":              body.get("id"),
            "paymentMethodId": body.get("paymentMethodId"),
            "amount":          body.get("amount"),
            "statusId":        body.get("statusId"),
            "transactionId":   body.get("transactionId", ""),
        }
        response = requests.put(
            f"{API_BASE}/UpdatePayment",
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


# ── DELETE PAYMENT ─────────────────────────────────────
@csrf_exempt
@require_http_methods(["POST"])
def delete_payment(request, payment_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.delete(
            f"{API_BASE}/DeletePayment?id={payment_id}",
            headers=_auth_headers(request),
            timeout=30,
        )
        try:
            data = response.json()
        except Exception:
            data = {"hasErrors": False}
        return JsonResponse(data, status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)