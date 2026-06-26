import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

API_BASE = settings.BUS_API_BASE

# ── Page view ─────────────────────────────────────────
def offices(request):
    return render(request, "dashboard/offices.html", {
        "token": request.session.get("bs_token", "")
    })


# ── Helper ────────────────────────────────────────────
def _auth_headers(request):
    token = request.session.get("bs_token", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept":        "application/json",
        "Content-Type":  "application/json",
    }


# ── GET all offices ───────────────────────────────────
def api_get_offices(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        res = requests.get(
            f"{API_BASE}/GetAllBusCompanyOffices",
            headers=_auth_headers(request),
        )
        # Pass through directly — same pattern as buses
        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── GET single office ─────────────────────────────────
def api_get_office(request, office_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        res = requests.get(
            f"{API_BASE}/GetBusCompanyOffice/{office_id}",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── CREATE office ─────────────────────────────────────
@csrf_exempt
def api_create_office(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        body = json.loads(request.body)
        print("CREATE OFFICE PAYLOAD:", body)

        res = requests.post(
            f"{API_BASE}/CreateBusCompanyOffice",
            headers=_auth_headers(request),
            json=body,
        )
        print("CREATE OFFICE STATUS:", res.status_code)
        print("CREATE OFFICE RESPONSE:", res.text)

        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── UPDATE office ─────────────────────────────────────
@csrf_exempt
def api_update_office(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        body = json.loads(request.body)
        print("UPDATE OFFICE PAYLOAD:", body)

        res = requests.post(
            f"{API_BASE}/UpdateBusCompanyOffice",
            headers=_auth_headers(request),
            json=body,
        )
        print("UPDATE OFFICE STATUS:", res.status_code)
        print("UPDATE OFFICE RESPONSE:", res.text)

        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── DELETE office ─────────────────────────────────────
@csrf_exempt
def api_delete_office(request, office_id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        res = requests.post(
            f"{API_BASE}/DeleteBusCompanyOffice/{office_id}",
            headers=_auth_headers(request),
        )
        print("DELETE OFFICE STATUS:", res.status_code)
        print("DELETE OFFICE RESPONSE:", res.text)

        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── GET all cities ───────────────────────────────────
def api_get_cities(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        res = requests.get(
            f"{API_BASE}/GetAllCities",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    


# ── GET all bus_company ───────────────────────────────────
def api_get_companies(request):
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