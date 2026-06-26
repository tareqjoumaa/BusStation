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
def assign_roles(request):
    return render(request, "dashboard/assign_roles.html", {
        "token": request.session.get("bs_token", "")
    })


# ── GET all users for role assignment ─────────────────
def api_get_users(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)
    try:
        res = requests.get(
            f"{API_BASE}/GetUsersForRoleAssignment",
            headers=_auth_headers(request),
        )
        print("GET USERS STATUS:", res.status_code)
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── GET roles of a specific user ──────────────────────
def api_get_user_roles(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)

    user_id = request.GET.get("userId")
    if not user_id:
        return JsonResponse({"error": "userId is required"}, status=400)

    try:
        res = requests.get(
            f"{API_BASE}/GetRolesOfUser",
            params={"userId": user_id},
            headers=_auth_headers(request),
        )
        print(f"GET ROLES OF USER [{user_id}] STATUS:", res.status_code)
        print(f"GET ROLES OF USER RESPONSE:", res.text)
        return JsonResponse(res.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ── ASSIGN roles to user ──────────────────────────────
@csrf_exempt
def api_assign_roles_to_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token"}, status=401)

    try:
        body = json.loads(request.body)
        print("=" * 60)
        print("ASSIGN ROLES TO USER PAYLOAD:", json.dumps(body, indent=2))

        res = requests.post(
            f"{API_BASE}/AddRolesToUser",
            headers=_auth_headers(request),
            json=body,
        )
        print("ASSIGN ROLES TO USER STATUS:", res.status_code)
        print("ASSIGN ROLES TO USER RESPONSE:", res.text)
        print("=" * 60)

        try:
            response_data = res.json()
        except Exception:
            response_data = {
                "result":           res.text,
                "hasErrors":        res.status_code >= 400,
                "validationErrors": []
            }

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        print("ASSIGN ROLES TO USER EXCEPTION:", str(e))
        return JsonResponse({"error": str(e)}, status=500)
