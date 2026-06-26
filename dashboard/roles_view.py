import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

API_BASE = settings.BUS_API_BASE


# ── Helper ────────────────────────────────────────────
def _auth_headers(request):
    token = request.session.get("bs_token", "")
    return {
        "Authorization": f"Bearer {token}",
        "Accept":        "application/json",
        "Content-Type":  "application/json",
    }


# ── Page view ─────────────────────────────────────────
def roles(request):
    return render(request, "dashboard/roles.html", {
        "token": request.session.get("bs_token", "")
    })


# ── GET all roles ─────────────────────────────────────
def api_get_roles(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetRoles",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── GET all claims (permissions) ──────────────────────
def api_get_all_claims(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetAllClaims",
            headers=_auth_headers(request),
        )
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── GET claims of a specific role ─────────────────────
def api_get_claims_of_role(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)

    role_id = request.GET.get("roleId")
    if not role_id:
        return JsonResponse({"error": "roleId is required"}, status=400)

    try:
        res = requests.get(
            f"{API_BASE}/GetClaimsOfRole",
            params={"roleId": role_id},
            headers=_auth_headers(request),
        )
        print(f"GetClaimsOfRole [{role_id}] → {res.status_code}")
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── CREATE role ───────────────────────────────────────
@csrf_exempt
def api_create_role(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)
    try:
        body = json.loads(request.body)
        print("CREATE ROLE PAYLOAD:", body)
        res = requests.post(
            f"{API_BASE}/CreateRole",
            headers=_auth_headers(request),
            json=body,
        )
        print("CREATE ROLE STATUS:", res.status_code)
        print("CREATE ROLE RESPONSE:", res.text)
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── ASSIGN claims to role ─────────────────────────────
@csrf_exempt
def api_assign_claims(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)
    try:
        body = json.loads(request.body)
        print("ASSIGN CLAIMS PAYLOAD:", body)
        res = requests.post(
            f"{API_BASE}/AssignClaimsToRole",
            headers=_auth_headers(request),
            json=body,
        )
        print("ASSIGN CLAIMS STATUS:", res.status_code)
        print("ASSIGN CLAIMS RESPONSE:", res.text)
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
