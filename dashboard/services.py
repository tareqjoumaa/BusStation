"""
services.py — Bus Station Admin Dashboard
All dummy data for dashboard views.
"""

import json


# ── Dashboard Stats ──────────────────────────────────────────────────────────
def get_stats():
    return {
        "total_reservations": 1248,
        "trips_today": 18,
        "available_buses": 12,
        "active_drivers": 24,
        "total_offices": 7,
        "monthly_revenue": 42800,
    }


# ── Bookings List ─────────────────────────────────────────────────────────────
def get_bookings():
    return [
        {"id": 1001, "customer_name": "Ahmad Al-Hassan", "passport": "SY-4821003",
         "trip_from": "Damascus", "trip_to": "Beirut", "date": "2026-04-05",
         "seat": "14A", "price": 45, "status": "Confirmed",
         "payment_status": "Paid", "phone": "+963-912-345678",
         "email": "ahmad@example.com", "nationality": "Syrian"},

        {"id": 1002, "customer_name": "Sara Khalil", "passport": "LB-9023411",
         "trip_from": "Beirut", "trip_to": "Amman", "date": "2026-04-05",
         "seat": "7B", "price": 65, "status": "Pending",
         "payment_status": "Unpaid", "phone": "+961-71-234567",
         "email": "sara@example.com", "nationality": "Lebanese"},

        {"id": 1003, "customer_name": "Omar Farouq", "passport": "JO-7812345",
         "trip_from": "Amman", "trip_to": "Istanbul", "date": "2026-04-06",
         "seat": "22C", "price": 120, "status": "Confirmed",
         "payment_status": "Paid", "phone": "+962-79-876543",
         "email": "omar@example.com", "nationality": "Jordanian"},

        {"id": 1004, "customer_name": "Lina Mourad", "passport": "SY-3310928",
         "trip_from": "Aleppo", "trip_to": "Latakia", "date": "2026-04-04",
         "seat": "3A", "price": 25, "status": "Completed",
         "payment_status": "Paid", "phone": "+963-944-123456",
         "email": "lina@example.com", "nationality": "Syrian"},

        {"id": 1005, "customer_name": "Karim Nassif", "passport": "LB-6620193",
         "trip_from": "Homs", "trip_to": "Damascus", "date": "2026-04-04",
         "seat": "11D", "price": 15, "status": "Cancelled",
         "payment_status": "Refunded", "phone": "+961-03-987654",
         "email": "karim@example.com", "nationality": "Lebanese"},

        {"id": 1006, "customer_name": "Nour Al-Din", "passport": "IQ-1122334",
         "trip_from": "Damascus", "trip_to": "Baghdad", "date": "2026-04-07",
         "seat": "18B", "price": 85, "status": "Confirmed",
         "payment_status": "Paid", "phone": "+964-770-112233",
         "email": "nour@example.com", "nationality": "Iraqi"},

        {"id": 1007, "customer_name": "Rania Saleh", "passport": "SY-8834521",
         "trip_from": "Latakia", "trip_to": "Beirut", "date": "2026-04-08",
         "seat": "5C", "price": 55, "status": "Pending",
         "payment_status": "Unpaid", "phone": "+963-933-445566",
         "email": "rania@example.com", "nationality": "Syrian"},

        {"id": 1008, "customer_name": "Tarek Ibrahim", "passport": "JO-4456789",
         "trip_from": "Amman", "trip_to": "Damascus", "date": "2026-04-09",
         "seat": "9A", "price": 40, "status": "Confirmed",
         "payment_status": "Paid", "phone": "+962-78-223344",
         "email": "tarek@example.com", "nationality": "Jordanian"},
    ]


# ── Booking Detail ────────────────────────────────────────────────────────────
def get_booking_detail(booking_id):
    bookings = get_bookings()
    booking = next((b for b in bookings if b["id"] == int(booking_id)), None)
    if not booking:
        return None

    booking.update({
        "departure_time": "08:30",
        "arrival_time": "12:45",
        "bus_number": "SY-BUS-2241",
        "bus_type": "VIP Luxury",
        "bus_seats": 48,
        "driver_name": "Hassan Mahmoud",
        "driver_license": "DL-SY-990112",
        "office_name": "Damascus Central",
        "office_country": "Syria",
        "office_city": "Damascus",
        "office_manager": "Khalid Al-Rashid",
        "payment_method": "Credit Card",
        "transaction_id": f"TXN-{booking_id}-20260405",
    })
    return booking


# ── Offices ───────────────────────────────────────────────────────────────────
def get_offices():
    return [
        {"id": 1, "city": "Damascus", "country": "Syria", "manager": "Khalid Al-Rashid",
         "active_trips": 8, "employees_count": 12, "buses_count": 5, "status": "Active"},
        {"id": 2, "city": "Aleppo", "country": "Syria", "manager": "Mariam Jouni",
         "active_trips": 4, "employees_count": 8, "buses_count": 3, "status": "Active"},
        {"id": 3, "city": "Beirut", "country": "Lebanon", "manager": "George Haddad",
         "active_trips": 6, "employees_count": 10, "buses_count": 4, "status": "Active"},
        {"id": 4, "city": "Amman", "country": "Jordan", "manager": "Sami Al-Zoubi",
         "active_trips": 3, "employees_count": 7, "buses_count": 3, "status": "Active"},
        {"id": 5, "city": "Homs", "country": "Syria", "manager": "Fadi Nassar",
         "active_trips": 2, "employees_count": 5, "buses_count": 2, "status": "Active"},
        {"id": 6, "city": "Latakia", "country": "Syria", "manager": "Rana Barakat",
         "active_trips": 1, "employees_count": 4, "buses_count": 1, "status": "Active"},
        {"id": 7, "city": "Istanbul", "country": "Turkey", "manager": "Mehmet Yilmaz",
         "active_trips": 2, "employees_count": 6, "buses_count": 2, "status": "Active"},
    ]


# ── Buses ─────────────────────────────────────────────────────────────────────
def get_buses():
    return [
        {"number": "SY-2241", "type": "VIP", "seats": 48, "occupancy": 87,
         "driver": "Hassan Mahmoud", "route_from": "Damascus", "route_to": "Beirut",
         "status": "Active", "maintenance": False},
        {"number": "SY-2242", "type": "Standard", "seats": 52, "occupancy": 62,
         "driver": "Samer Khalil", "route_from": "Aleppo", "route_to": "Latakia",
         "status": "Active", "maintenance": False},
        {"number": "SY-2243", "type": "Express", "seats": 36, "occupancy": 94,
         "driver": "Faris Atallah", "route_from": "Damascus", "route_to": "Amman",
         "status": "Active", "maintenance": True},
        {"number": "LB-3301", "type": "VIP", "seats": 44, "occupancy": 75,
         "driver": "Antoine Khoury", "route_from": "Beirut", "route_to": "Amman",
         "status": "Active", "maintenance": False},
        {"number": "LB-3302", "type": "Standard", "seats": 52, "occupancy": 50,
         "driver": "Michel Azar", "route_from": "Beirut", "route_to": "Damascus",
         "status": "Maintenance", "maintenance": True},
        {"number": "JO-4401", "type": "Express", "seats": 40, "occupancy": 80,
         "driver": "Rami Haddad", "route_from": "Amman", "route_to": "Istanbul",
         "status": "Active", "maintenance": False},
    ]


# ── Employees ─────────────────────────────────────────────────────────────────
def get_employees():
    return [
        {"id": 1, "name": "Hassan Mahmoud", "role": "Driver", "office": "Damascus Central",
         "phone": "+963-911-111111", "assigned_bus": "SY-2241",
         "route": "Damascus → Beirut", "performance": 92},
        {"id": 2, "name": "Samer Khalil", "role": "Driver", "office": "Aleppo Branch",
         "phone": "+963-922-222222", "assigned_bus": "SY-2242",
         "route": "Aleppo → Latakia", "performance": 88},
        {"id": 3, "name": "Khalid Al-Rashid", "role": "Manager", "office": "Damascus Central",
         "phone": "+963-933-333333", "assigned_bus": "—",
         "route": "—", "performance": 97},
        {"id": 4, "name": "Mariam Jouni", "role": "Manager", "office": "Aleppo Branch",
         "phone": "+963-944-444444", "assigned_bus": "—",
         "route": "—", "performance": 95},
        {"id": 5, "name": "Rana Barakat", "role": "Office Staff", "office": "Latakia Office",
         "phone": "+963-955-555555", "assigned_bus": "—",
         "route": "—", "performance": 84},
        {"id": 6, "name": "Faris Atallah", "role": "Driver", "office": "Damascus Central",
         "phone": "+963-966-666666", "assigned_bus": "SY-2243",
         "route": "Damascus → Amman", "performance": 79},
        {"id": 7, "name": "George Haddad", "role": "Manager", "office": "Beirut Branch",
         "phone": "+961-71-777777", "assigned_bus": "—",
         "route": "—", "performance": 91},
        {"id": 8, "name": "Lara Nassif", "role": "Office Staff", "office": "Beirut Branch",
         "phone": "+961-03-888888", "assigned_bus": "—",
         "route": "—", "performance": 86},
    ]


# ── Chart Data ────────────────────────────────────────────────────────────────
def get_chart_data():
    labels = ["Apr 1","Apr 2","Apr 3","Apr 4","Apr 5","Apr 6","Apr 7",
              "Apr 8","Apr 9","Apr 10","Apr 11","Apr 12","Apr 13","Apr 14"]

    reservations = [
        {"label": l,
         "confirmed": c,
         "completed": cp}
        for l, c, cp in zip(
            labels,
            [22, 35, 28, 40, 18, 45, 52, 38, 60, 42, 55, 48, 70, 63],
            [15, 22, 18, 30, 12, 35, 40, 28, 45, 32, 44, 38, 58, 50]
        )
    ]

    revenue_months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    revenue = [
        {"label": m, "value": v}
        for m, v in zip(revenue_months, [24500, 21800, 32100, 19400, 28700, 42800])
    ]

    routes = [
        {"label": "Damascus→Beirut",   "value": 34},
        {"label": "Beirut→Amman",      "value": 22},
        {"label": "Damascus→Istanbul", "value": 18},
        {"label": "Amman→Damascus",    "value": 14},
        {"label": "Aleppo→Latakia",    "value": 8},
        {"label": "Other",             "value": 4},
    ]

    occupancy = [
        {"label": "VIP Fleet",      "value": 87},
        {"label": "Express Fleet",  "value": 82},
        {"label": "Standard Fleet", "value": 65},
        {"label": "Old Fleet",      "value": 51},
    ]

    statuses = {
        "confirmed": 620,
        "pending":   215,
        "cancelled":  98,
        "completed": 315,
    }

    return {
        "reservations": json.dumps(reservations),
        "revenue":      json.dumps(revenue),
        "routes":       json.dumps(routes),
        "occupancy":    json.dumps(occupancy),
        "statuses":     json.dumps(statuses),
    }


# ── Activity Feed ─────────────────────────────────────────────────────────────
def get_activities():
    return [
        {"type": "booking", "icon": "fas fa-ticket-alt",
         "message": "New reservation #1008 created for Tarek Ibrahim",
         "time": "2 minutes ago"},
        {"type": "trip", "icon": "fas fa-bus",
         "message": "Trip SY-2241 departed Damascus — on schedule",
         "time": "14 minutes ago"},
        {"type": "cancel", "icon": "fas fa-times-circle",
         "message": "Reservation #1005 cancelled by Karim Nassif",
         "time": "38 minutes ago"},
        {"type": "staff", "icon": "fas fa-user",
         "message": "Driver Hassan Mahmoud checked in at Damascus terminal",
         "time": "1 hour ago"},
        {"type": "trip", "icon": "fas fa-flag-checkered",
         "message": "Trip LB-3301 arrived Amman — completed",
         "time": "2 hours ago"},
        {"type": "booking", "icon": "fas fa-ticket-alt",
         "message": "New reservation #1007 created for Rania Saleh",
         "time": "3 hours ago"},
    ]


# ── Alerts ────────────────────────────────────────────────────────────────────
def get_alerts():
    return [
        {"level": "warning", "icon": "fas fa-wrench",
         "title": "Maintenance Due", "description": "Bus SY-2243 — service due in 3 days"},
        {"level": "danger", "icon": "fas fa-exclamation-circle",
         "title": "Maintenance Overdue", "description": "Bus LB-3302 — overdue by 8 days"},
        {"level": "info", "icon": "fas fa-passport",
         "title": "Visa Check Required", "description": "3 passengers on route to Turkey"},
    ]


# ── Monthly Report ────────────────────────────────────────────────────────────
def get_monthly_report():
    return [
        {"month": "January",   "tickets": 210, "revenue": 19400, "expenses": 8200,  "profit": 11200, "growth": -5.2},
        {"month": "February",  "tickets": 285, "revenue": 28700, "expenses": 9100,  "profit": 19600, "growth": 47.9},
        {"month": "March",     "tickets": 402, "revenue": 42800, "expenses": 11300, "profit": 31500, "growth": 49.2},
        {"month": "April",     "tickets": 380, "revenue": 38200, "expenses": 10800, "profit": 27400, "growth": -10.7},
        {"month": "May",       "tickets": 445, "revenue": 45600, "expenses": 12100, "profit": 33500, "growth": 19.4},
        {"month": "June",      "tickets": 510, "revenue": 53800, "expenses": 13200, "profit": 40600, "growth": 18.0},
    ]
