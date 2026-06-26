"""
login_view.py — Bus Station Admin
API call happens here on the server (avoids browser CORS).
"""

import requests
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from functools import wraps

from django.conf import settings

API_BASE = settings.BUS_API_BASE
API_LOGIN_URL = f'{API_BASE}/Login'


@require_http_methods(["GET", "POST"])
@csrf_protect
def login_view(request):

    # Already logged in → go to dashboard
    if request.session.get('bs_token'):
        return redirect('dashboard:home')

    if request.method == 'GET':
        return render(request, 'dashboard/login.html')

    # ── POST: call the real API from Django server ────────────────────────────
    phone_number = request.POST.get('phoneNumber', '').strip()
    password     = request.POST.get('password', '').strip()

    if not phone_number or not password:
        return render(request, 'dashboard/login.html', {
            'error': 'Phone number and password are required.',
            'phone_number': phone_number,
        })

    try:
        response = requests.post(
            API_LOGIN_URL,
            json={'phoneNumber': phone_number, 'password': password},
            headers={'Content-Type': 'application/json', 'Accept': '*/*'},
            timeout=10,
        )

        data = response.json()
        result = data.get('result') or {}

        if response.status_code == 200 \
                and not data.get('hasErrors') \
                and result.get('token'):

            result = data['result']
            request.session['bs_token']     = result['token']
            request.session['bs_role'] = ','.join(result.get('role') or [])
            request.session['bs_user_type'] = str(result.get('userTypeId', ''))
            request.session['bs_phone']     = phone_number
            request.session.set_expiry(86400)  # 24 hours
            return redirect('dashboard:home')

        # API returned error message
        errors = data.get('validationErrors', [])
        error_msg = errors[0].get('description', 'Invalid credentials.') \
            if errors else 'Invalid phone number or password.'

        return render(request, 'dashboard/login.html', {
            'error': error_msg,
            'phone_number': phone_number,
        })

    except requests.exceptions.ConnectionError:
        return render(request, 'dashboard/login.html', {
            'error': 'Cannot connect to the authentication server. Please try again.',
            'phone_number': phone_number,
        })
    except requests.exceptions.Timeout:
        return render(request, 'dashboard/login.html', {
            'error': 'Server took too long to respond. Please try again.',
            'phone_number': phone_number,
        })

    except Exception as e:
        import traceback

        print("🔥 ERROR TRACE:")
        print(traceback.format_exc())

        return render(request, 'dashboard/login.html', {
            'error': f'Unexpected error: {str(e)}',
            'phone_number': phone_number,
        })  


def logout_view(request):
    request.session.flush()
    return redirect('dashboard:login')


# ── Decorator to protect dashboard views ─────────────────────────────────────
def login_required_api(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.session.get('bs_token'):
            return redirect('dashboard:login')
        return view_func(request, *args, **kwargs)
    return _wrapped


def get_auth_headers(request):
    """Pass this to any future requests.get/post calls to the API."""
    return {
        'Authorization': f'Bearer {request.session.get("bs_token", "")}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }