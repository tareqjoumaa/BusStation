import json
import requests

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

API_BASE = settings.BUS_API_BASE


# ───────────────────────────────────────
# PAGE
# ───────────────────────────────────────

def customer(request):
    return render(request, 'dashboard/customer.html')


# ───────────────────────────────────────
# HELPERS
# ───────────────────────────────────────

def _auth_headers(request):
    token = request.session.get("bs_token", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


# ───────────────────────────────────────
# GET ALL CUSTOMERS
# ───────────────────────────────────────

def api_get_customers(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetAllCustomers",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# GET CUSTOMER
# ───────────────────────────────────────

def api_get_customer(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    customer_id = request.GET.get("customerId")
    try:
        res = requests.get(
            f"{API_BASE}/GetCustomer",
            params={"customerId": customer_id},
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# GET GENDERS
# ───────────────────────────────────────

def api_get_genders(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetGenders",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# CREATE CUSTOMER
# ───────────────────────────────────────

@csrf_exempt
def api_create_customer(request):
    print("=== api_create_customer HIT ===")  # add this as line 1

    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    print(f"tooooken is {token}")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body)
        res = requests.post(
            f"{API_BASE}/CreateCustomer",
            headers=_auth_headers(request),
            json=body,
        )
        print(f"res is {res}")

        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# EDIT CUSTOMER
# ───────────────────────────────────────

@csrf_exempt
def api_edit_customer(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    token = request.session.get("bs_token")

    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        body = json.loads(request.body)

        print("EDIT BODY:", body)

        res = requests.post(
            f"{API_BASE}/EditCustomer",
            headers=_auth_headers(request),
            json=body,
        )

        print("STATUS:", res.status_code)
        print("RESPONSE:", res.text)

        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        print("EDIT ERROR:", str(e))
        return JsonResponse({"error": str(e)}, status=500)
    

# ───────────────────────────────────────
# DELETE CUSTOMER
# ───────────────────────────────────────

@csrf_exempt
def api_delete_customer(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body)
        res = requests.post(
            f"{API_BASE}/DeleteAccount",
            headers=_auth_headers(request),
            json=body,
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
