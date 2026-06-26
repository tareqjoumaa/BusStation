"""
views.py — Bus Station Admin Dashboard
"""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .login_view import login_required_api
from . import services

@login_required_api
def home(request):
    """Main dashboard overview page."""
    context = {
        "stats":       services.get_stats(),
        "bookings":    services.get_bookings()[:6],
        "chart_data":  services.get_chart_data(),
        "activities":  services.get_activities(),
        "alerts":      services.get_alerts(),
    }
    return render(request, "dashboard/home.html", context)


@login_required_api
def reservations(request):
    """Full reservations management page."""
    context = {
        "bookings": services.get_bookings(),
    }
    return render(request, "dashboard/reservations.html", context)


@login_required_api
def reservation_detail(request, booking_id):
    """Reservation detail page."""
    booking = services.get_booking_detail(booking_id)
    if not booking:
        raise Http404("Reservation not found")
    context = {
        "booking": booking,
    }
    return render(request, "dashboard/reservation_detail.html", context)


@login_required_api
def offices(request):
    """Office management page."""
    context = {
        "offices": services.get_offices(),
    }
    return render(request, "dashboard/offices.html", context)


@login_required_api
def buses(request):
    """Bus fleet management page."""
    context = {
        "buses": services.get_buses(),
    }
    return render(request, "dashboard/buses.html", context)


@login_required_api
def employees(request):
    """Employee management page."""
    context = {
        "employees": services.get_employees(),
    }
    return render(request, "dashboard/employees.html", context)


@login_required_api
def reports(request):
    """Financial reports page."""
    context = {
        "monthly_report": services.get_monthly_report(),
    }
    return render(request, "dashboard/reports.html", context)
