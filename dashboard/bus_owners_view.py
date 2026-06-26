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

def bus_owners_page(request):
    return render(request, 'dashboard/bus_owners.html')


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
# GET ALL BUS OWNERS
# ───────────────────────────────────────

def api_get_bus_owners(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetAllBusCompanyOwners",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# GET SINGLE BUS OWNER
# ───────────────────────────────────────

def api_get_bus_owner(request, owner_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetBusCompanyOwner/{owner_id}",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# CREATE BUS OWNER
# ───────────────────────────────────────

@csrf_exempt
def api_create_bus_owner(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body)
        res = requests.post(
            f"{API_BASE}/CreateBusCompanyOwner",
            headers=_auth_headers(request),
            json=body,
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# UPDATE BUS OWNER
# ───────────────────────────────────────

@csrf_exempt
def api_update_bus_owner(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body)
        res = requests.post(
            f"{API_BASE}/UpdateBusCompanyOwner",
            headers=_auth_headers(request),
            json=body,
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# DELETE BUS OWNER
# ───────────────────────────────────────

@csrf_exempt
def api_delete_bus_owner(request, owner_id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        res = requests.post(
            f"{API_BASE}/DeleteBusCompanyOwner/{owner_id}",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
