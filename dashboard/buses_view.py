import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

API_BASE = settings.BUS_API_BASE

# ───────────────────────────────────────
# Page Views
# ───────────────────────────────────────

def buses(request):
    return render(request, "dashboard/buses.html", {
        "token": request.session.get("token", "")
    })


def bus_create(request):
    return render(request, "dashboard/bus_create.html", {
        "token": request.session.get("token", "")
    })


# ───────────────────────────────────────
# API: Get Buses
# ───────────────────────────────────────

def api_get_buses(request):
    token = request.session.get("bs_token")
    print("SESSION TOKEN:", token)

    if not token:
        return JsonResponse({"error": "No token found in session"}, status=401)

    try:
        res = requests.get(
            f"{API_BASE}/GetAllBuses",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json"
            }
        )
        return JsonResponse(res.json(), safe=False)


    except Exception as e:
        print("ERROR:", str(e))
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# API: Get Offices
# ───────────────────────────────────────

def api_get_offices(request):
    token = request.session.get("bs_token")

    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        res = requests.get(
            f"{API_BASE}/GetAllBusCompanyOffices",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json"
            }
        )
        data = res.json()

        return JsonResponse(data.get("result", []), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ───────────────────────────────────────
# API: Create Bus
# ───────────────────────────────────────

@csrf_exempt
def api_create_bus(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    token = request.session.get("bs_token")

    if not token:
        return JsonResponse({"error": "No token found"}, status=401)

    try:
        res = requests.post(
            f"{API_BASE}/CreateBus",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            data=request.body
        )

        print("STATUS:", res.status_code)
        print("RESPONSE:", res.text)

        return JsonResponse(res.json(), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



# ───────────────────────────────────────
# API: Delete Bus
# Add this to your buses_view.py
# ───────────────────────────────────────    


@csrf_exempt
def api_delete_bus(request, bus_id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)
 
    token = request.session.get("bs_token")
    if not token:
        return JsonResponse({"error": "No token found"}, status=401)
 
    try:
        res = requests.post(
            f"{API_BASE}/DeleteBus/{bus_id}",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            }
        )
        return JsonResponse(res.json(), safe=False)
 
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)