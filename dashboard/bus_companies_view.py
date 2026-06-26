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

def bus_companies_page(request):
    return render(request, 'dashboard/bus_companies.html')


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
# GET ALL BUS COMPANIES
# ───────────────────────────────────────

def api_get_bus_companies(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetAllBusCompanies",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# GET SINGLE BUS COMPANY
# ───────────────────────────────────────

def api_get_bus_company(request, company_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetBusCompany/{company_id}",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# CREATE BUS COMPANY
# ───────────────────────────────────────

@csrf_exempt
def api_create_bus_company(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body)
        res = requests.post(
            f"{API_BASE}/CreateBusCompany",
            headers=_auth_headers(request),
            json=body,
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# UPDATE BUS COMPANY
# ───────────────────────────────────────

@csrf_exempt
def api_update_bus_company(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body)
        res = requests.post(
            f"{API_BASE}/UpdateBusCompany",
            headers=_auth_headers(request),
            json=body,
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# DELETE BUS COMPANY
# ───────────────────────────────────────

@csrf_exempt
def api_delete_bus_company(request, company_id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.post(
            f"{API_BASE}/DeleteBusCompany/{company_id}",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
