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

def employees_page(request):
    return render(request, "dashboard/bus_employees.html")


# =========================================================
# GET ALL EMPLOYEES
# =========================================================

@require_http_methods(["GET"])
def get_employees(request):
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
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)


# =========================================================
# GET SINGLE EMPLOYEE
# =========================================================

@require_http_methods(["GET"])
def get_employee(request, employee_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetBusCompanyEmployee/{employee_id}",
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
# GET ALL EMPLOYEE TYPES  ← dedicated endpoint
# =========================================================

@require_http_methods(["GET"])
def get_employee_types(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBusCompanyEmployeeTypes",
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
# CREATE EMPLOYEE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def create_employee(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))

        # firstIdImage / secondIdImage arrive as pure base64 strings (data: prefix already stripped)
        # firstIdImageExtension / secondIdImageExtension arrive as e.g. "jpg", "png", "webp"
        payload = {
            "email":                    body.get("email"),
            "password":                 body.get("password"),
            "phoneNumber":              body.get("phoneNumber"),
            "busCompanyEmployeeTypeId": body.get("busCompanyEmployeeTypeId"),
            "firstName":                body.get("firstName"),
            "lastName":                 body.get("lastName"),
            "firstIdImage":             body.get("firstIdImage"),
            "firstIdImageExtension":    f".{body.get('firstIdImageExtension')}" if body.get("firstIdImageExtension") else None,
            "secondIdImage":            body.get("secondIdImage"),
            "secondIdImageExtension":   f".{body.get('secondIdImageExtension')}" if body.get("secondIdImageExtension") else None,
            "busCompanyOfficeId":       body.get("busCompanyOfficeId"),
        }

        json_payload = json.dumps(payload, ensure_ascii=False)
        response = requests.post(
            f"{API_BASE}/CreateBusCompanyEmployee",
            json=payload,
            headers=_auth_headers(request),
            timeout=60,
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
# UPDATE EMPLOYEE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def update_employee(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        body = json.loads(request.body.decode("utf-8"))

        payload = {
            "id":                       body.get("id"),
            "phoneNumber":              body.get("phoneNumber"),
            "busCompanyEmployeeTypeId": body.get("busCompanyEmployeeTypeId"),
            "firstName":                body.get("firstName"),
            "lastName":                 body.get("lastName"),
            "email":                    body.get("email"),
            "busCompanyOfficeId":       body.get("busCompanyOfficeId"),
            "removeFirstIdImage":       body.get("removeFirstIdImage", False),
            "removeSecondIdImage":      body.get("removeSecondIdImage", False),
        }

        # Only include image fields when a new image was actually uploaded
        if body.get("firstIdImage"):
            payload["firstIdImage"]          = body.get("firstIdImage")
            payload["firstIdImageExtension"] = (
                f".{body.get('firstIdImageExtension')}"
                if body.get("firstIdImageExtension")
                else None
            )
        if body.get("secondIdImage"):
            payload["secondIdImage"]          = body.get("secondIdImage")
            payload["secondIdImageExtension"] = (
                f".{body.get('secondIdImageExtension')}"
                if body.get("secondIdImageExtension")
                else None
            )

        json_payload = json.dumps(payload, ensure_ascii=False)

        response = requests.post(
            f"{API_BASE}/UpdateBusCompanyEmployee",
            data=json_payload,
            headers=_auth_headers(request),
            timeout=60,
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
# DELETE EMPLOYEE
# =========================================================

@csrf_exempt
@require_http_methods(["POST"])
def delete_employee(request, employee_id):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.post(
            f"{API_BASE}/DeleteBusCompanyEmployee/{employee_id}",
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
# GET ALL OFFICES
# =========================================================

@require_http_methods(["GET"])
def get_offices(request):
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
    try:
        response = requests.get(
            f"{API_BASE}/GetAllBusCompanyOffices",
            headers=_auth_headers(request),
            timeout=30,
        )
        data = response.json()
        return JsonResponse(data, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e), "hasErrors": True}, status=500)