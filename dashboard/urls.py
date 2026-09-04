"""
urls.py — Bus Station Admin Dashboard
"""

from django.urls import path
from . import views
from . import login_view
from . import buses_view
from . import offices_view
from . import roles_view
from . import assign_roles_view
from . import customers_view
from . import location_view
from . import bus_owners_view
from . import bus_companies_view
from . import bus_employees_views
from . import bus_routes_views
from . import trip_schedules_views
from . import trip_instances_views
from . import bookings_views
from . import trip_detail_views
from . import payments_views

app_name = "dashboard"

urlpatterns = [
    # ── Auth ─────────────────────────────
    path("login/",  login_view.login_view,  name="login"),
    path("logout/", login_view.logout_view, name="logout"),

    # ── Pages ────────────────────────────
    path("", bookings_views.bookings_page, name="bookings"),
    path("reservations/", views.reservations, name="reservations"),
    path("reservations/<int:booking_id>/", views.reservation_detail, name="reservation_detail"),
    path("offices/", views.offices, name="offices"),
    path("buses/", views.buses, name="buses"),
    path("buses/create/", buses_view.bus_create, name="bus_create"),  
    path("employees/", views.employees, name="employees"),
    path("reports/", views.reports, name="reports"),

    # ── BUS ─────────────────
    path('api/buses/', buses_view.api_get_buses, name='api_buses'),
    path('api/offices/', buses_view.api_get_offices, name='api_offices'),
    path('api/buses/create/', buses_view.api_create_bus, name='api_create_bus'),
    path("api/buses/<int:bus_id>/delete/", buses_view.api_delete_bus, name="api_delete_bus"),


    # ── Offices ─────────────────
    path("offices/",  offices_view.offices, name="offices"),
    path("api/offices/",                          offices_view.api_get_offices,    name="api_get_offices"),
    path("api/offices/<int:office_id>/",          offices_view.api_get_office,     name="api_get_office"),
    path("api/offices/create/",                   offices_view.api_create_office,  name="api_create_office"),
    path("api/offices/update/",                   offices_view.api_update_office,  name="api_update_office"),
    path("api/offices/<int:office_id>/delete/",   offices_view.api_delete_office,  name="api_delete_office"),

    # ── City ─────────────────
    path("api/cities/", offices_view.api_get_cities, name="api_get_cities"),

    # ── Companies ─────────────────────────────
    path("api/companies/", offices_view.api_get_companies, name="api_get_companies"),

    # ── Roles and permssions ─────────────────────────────
    path("roles/",                      roles_view.roles,                name="roles"),
    path("api/roles/",                  roles_view.api_get_roles,        name="api_get_roles"),
    path("api/roles/claims/",           roles_view.api_get_all_claims,   name="api_get_all_claims"),
    path("api/roles/claims-of-role/",   roles_view.api_get_claims_of_role, name="api_get_claims_of_role"),
    path("api/roles/create/",           roles_view.api_create_role,      name="api_create_role"),
    path("api/roles/assign-claims/",    roles_view.api_assign_claims,    name="api_assign_claims"),

    # ── Assign role ─────────────────────────────
    path("assign-roles/",              assign_roles_view.assign_roles,           name="assign_roles"),
    path("api/roles/users/",           assign_roles_view.api_get_users,          name="api_get_users"),
    path("api/roles/user-roles/",      assign_roles_view.api_get_user_roles,     name="api_get_user_roles"),
    path("api/roles/assign-to-user/",  assign_roles_view.api_assign_roles_to_user, name="api_assign_roles_to_user"),

    # ── Customers ─────────────────────────────

    path('customers/', customers_view.customer, name='customer'),
    path("api/customers/", customers_view.api_get_customers, name="api_get_customers"),
    path("api/customer/", customers_view.api_get_customer, name="api_get_customer"),
    path("api/genders/", customers_view.api_get_genders, name="api_get_genders"),
    path("api/customers/create/", customers_view.api_create_customer, name="api_create_customer"),
    path("api/customers/edit/", customers_view.api_edit_customer, name="api_edit_customer"),
    path("api/customers/delete/", customers_view.api_delete_customer, name="api_delete_customer"),


    # ── Location ─────────────────────────────

    path('locations/', location_view.locations_page, name='location'),
    path('api/governorates/', location_view.get_governorates, name='get_governorates'),
    path('api/cities/', location_view.get_cities, name='get_cities'),
    path('api/cities/create/', location_view.create_city, name='create_city'),
    path('api/cities/update/', location_view.update_city, name='update_city'),

    # ── Bus Owners page ─────────────────────────────
    
    path('company/bus-owners/', bus_owners_view.bus_owners_page, name='bus_owners'),
    path('api/bus-owners/',              bus_owners_view.api_get_bus_owners,   name='api_get_bus_owners'),
    path('api/bus-owners/<int:owner_id>/', bus_owners_view.api_get_bus_owner,  name='api_get_bus_owner'),
    path('api/bus-owners/create/',       bus_owners_view.api_create_bus_owner, name='api_create_bus_owner'),
    path('api/bus-owners/update/',       bus_owners_view.api_update_bus_owner, name='api_update_bus_owner'),
    path('api/bus-owners/delete/<int:owner_id>/', bus_owners_view.api_delete_bus_owner, name='api_delete_bus_owner'),


    # ── Bus Companies page ─────────────────────────────

    path('company/bus-companies/', bus_companies_view.bus_companies_page, name='bus_companies'),
    path('api/bus-companies/create/',                  bus_companies_view.api_create_bus_company, name='api_create_bus_company'),
    path('api/bus-companies/update/',                  bus_companies_view.api_update_bus_company, name='api_update_bus_company'),
    path('api/bus-companies/delete/<int:company_id>/', bus_companies_view.api_delete_bus_company, name='api_delete_bus_company'),
    path('api/bus-companies/<int:company_id>/',        bus_companies_view.api_get_bus_company,    name='api_get_bus_company'),
    path('api/bus-companies/',                         bus_companies_view.api_get_bus_companies,  name='api_get_bus_companies'),

    # ── Employees ──────────────────────────────────────────────────────────────
    path("company/employees/",                       bus_employees_views.employees_page,     name="employees_page"), 
    path("api/employees/",                           bus_employees_views.get_employees,      name="get_employees"),
    path("api/employees/<int:employee_id>/",         bus_employees_views.get_employee,       name="get_employee"),
    path("api/employees/create/",                    bus_employees_views.create_employee,    name="create_employee"),
    path("api/employees/update/",                    bus_employees_views.update_employee,    name="update_employee"),
    path("api/employees/delete/<int:employee_id>/",  bus_employees_views.delete_employee,    name="delete_employee"),
    path("api/employee-types/",                      bus_employees_views.get_employee_types, name="get_employee_types"),
    path("api/offices/",                             bus_employees_views.get_offices,        name="get_offices"),

    # ── Routes ──────────────────────────────────────────────────────────────

    path("company/routes/",                      bus_routes_views.routes_page,           name="routes_page"),
    path("api/routes/",                          bus_routes_views.get_routes,            name="get_routes"),
    path("api/routes/<int:route_id>/",           bus_routes_views.get_route,             name="get_route"),
    path("api/routes/create/",                   bus_routes_views.create_route,          name="create_route"),
    path("api/routes/update/",                   bus_routes_views.update_route,          name="update_route"),
    path("api/routes/delete/<int:route_id>/",    bus_routes_views.delete_route,          name="delete_route"),
    path("api/routes/cities/",                   bus_routes_views.get_cities_for_routes, name="get_cities_for_routes"),
    path("api/routes/offices/",                  bus_routes_views.get_offices_for_routes,name="get_offices_for_routes"),

    # ── trip-schedules ──────────────────────────────────────────────────────────────

    path("company/trip-schedules/",                        trip_schedules_views.trip_schedules_page,   name="trip_schedules"),
    path("api/trip-schedules/",                            trip_schedules_views.get_trip_schedules,    name="get_trip_schedules"),
    path("api/trip-schedules/<int:trip_id>/",              trip_schedules_views.get_trip_schedule,     name="get_trip_schedule"),
    path("api/trip-schedules/create/",                     trip_schedules_views.create_trip_schedule,  name="create_trip_schedule"),
    path("api/trip-schedules/update/",                     trip_schedules_views.update_trip_schedule,  name="update_trip_schedule"),
    path("api/trip-schedules/delete/<int:trip_id>/",       trip_schedules_views.delete_trip_schedule,  name="delete_trip_schedule"),
    path("api/trip-schedules/routes/",                     trip_schedules_views.get_routes_for_trips,  name="get_routes_for_trips"),
    path("api/trip-schedules/buses/",                      trip_schedules_views.get_buses_for_trips,   name="get_buses_for_trips"),
    path("api/trip-schedules/drivers/",                    trip_schedules_views.get_drivers_for_schedules, name="get_drivers_for_schedules"),

    # ── trip-instance ──────────────────────────────────────────────────────────────

    path("company/my-trips/",                            trip_instances_views.trip_instances_page,       name="trip_instances"),
    path("api/trip-instances/",                          trip_instances_views.get_trip_instances,        name="get_trip_instances"),
    path("api/trip-instances/<int:trip_id>/",            trip_instances_views.get_trip_instance,         name="get_trip_instance"),
    path("api/trip-instances/schedules/",                trip_instances_views.get_schedules_for_instances, name="get_schedules_for_instances"),
    path("api/trip-instances/companies/",                trip_instances_views.get_companies_for_instances, name="get_companies_for_instances"),

    # ── bookings ──────────────────────────────────────────────────────────────

    path("bookings/",                                       bookings_views.bookings_page,            name="bookings"),
    path("api/bookings/",                                   bookings_views.get_bookings,             name="get_bookings"),
    path("api/bookings/<int:booking_id>/",                  bookings_views.get_booking,              name="get_booking"),
    path("api/bookings/by-trip/<int:trip_id>/",             bookings_views.get_bookings_by_trip,     name="get_bookings_by_trip"),
    path("api/bookings/create/",                            bookings_views.create_booking,           name="create_booking"),
    path("api/bookings/update/",                            bookings_views.update_booking,           name="update_booking"),
    path("api/bookings/cancel/<int:booking_id>/",           bookings_views.cancel_booking,           name="cancel_booking"),
    path("api/bookings/trips/",                             bookings_views.get_trips_for_bookings,   name="get_trips_for_bookings"),
    path("api/bookings/trip-instance/<int:trip_id>/", bookings_views.get_trip_instance_for_booking, name="get_trip_instance_for_booking"),

    # ── trip-detail ──────────────────────────────────────────────────────────────

    path("company/my-trips/<int:trip_id>/",           trip_detail_views.trip_detail_page,  name="trip_detail"),
    path("api/trip-detail/<int:trip_id>/",            trip_detail_views.get_trip_detail,   name="get_trip_detail"),
    path("api/trip-detail/<int:trip_id>/seats/",      trip_detail_views.get_trip_seats,    name="get_trip_seats"),
    path("api/trip-detail/drivers/",                  trip_detail_views.get_drivers,       name="get_drivers"),
    path("api/trip-detail/assign-driver/",            trip_detail_views.assign_driver,     name="assign_driver"),


    # ── Payments ─────────────────────────────────────────────────────────────────

    path("payments/",                              payments_views.payments_page,           name="payments"),
    path("api/payments/",                          payments_views.get_payments,            name="get_payments"),
    path("api/payments/methods/",                  payments_views.get_payment_methods,     name="get_payment_methods"),
    path("api/payments/statuses/",                 payments_views.get_payment_statuses,    name="get_payment_statuses"),
    path("api/payments/bookings/",                 payments_views.get_bookings_for_payments, name="get_bookings_for_payments"),
    path("api/payments/create/",                   payments_views.create_payment,          name="create_payment"),
    path("api/payments/update/",                   payments_views.update_payment,          name="update_payment"),
    path("api/payments/delete/<int:payment_id>/",  payments_views.delete_payment,          name="delete_payment"),
]
