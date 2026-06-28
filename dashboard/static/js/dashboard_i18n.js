/* ================================================================
   BUS STATION DASHBOARD — Internationalization (i18n)
   Supports: English (en) | Arabic (ar)
   Usage: loaded in base.html, no changes needed in child pages.
   Language stored in localStorage so it persists across pages.
================================================================ */

const TRANSLATIONS = {
  en: {
    // ── Brand ──────────────────────────────────────────
    brand_name:    'BusStation',
    brand_sub:     'Admin Portal',

    // ── Sidebar section labels ──────────────────────────
    section_operations:   'Operations',
    section_management:   'Management',
    section_admin:        'Administration',

    // ── Nav items ───────────────────────────────────────
    nav_overview:         'Overview',
    nav_routes:           'Routes',
    nav_trip_schedules:   'Trip Schedules',
    nav_my_trips:         'My Trips',
    nav_bookings:         'Bookings',
    nav_payments:         'Payments',
    nav_fleet:            'Fleet',
    nav_company:          'Company',
    nav_bus_owners:       'Bus Owners',
    nav_bus_companies:    'Bus Companies',
    nav_offices:          'Company Offices',
    nav_employees:        'Employees',
    nav_customers:        'Customers',
    nav_location:         'Location',
    nav_reports:          'Reports',
    nav_roles:            'Roles & Permissions',
    nav_assign_roles:     'Assign Roles',

    // ── Topbar ──────────────────────────────────────────
    search_placeholder:   'Search anything...',
    admin_name:           'Admin',
    admin_role:           'Super Admin',

    // ── Toolbar shared ──────────────────────────────────
    btn_refresh:          'Refresh',
    btn_new_booking:      'New Booking',
    btn_new_schedule:     'New Schedule',
    btn_new_route:        'New Route',
    btn_new_employee:     'New Employee',
    btn_save:             'Save Changes',
    btn_cancel:           'Cancel',
    btn_close:            'Close',
    btn_edit:             'Edit',
    btn_delete:           'Delete',
    btn_create:           'Create',
    btn_yes_cancel:       'Yes, Cancel',
    btn_keep:             'Keep Booking',

    // ── Common table headers ─────────────────────────────
    th_id:          'ID',
    th_status:      'Status',
    th_actions:     'Actions',
    th_created:     'Created',
    th_date:        'Date',
    th_price:       'Price',

    // ── Bookings page ───────────────────────────────────
    page_bookings:        'Bookings',
    kpi_total_bookings:   'Total Bookings',
    kpi_confirmed:        'Confirmed',
    kpi_cancelled:        'Cancelled',
    kpi_showing:          'Showing',
    filter_all_statuses:  'All Statuses',
    filter_confirmed:     'Confirmed',
    filter_reserved:      'Reserved',
    filter_cancelled:     'Cancelled',
    filter_pending:       'Pending',
    filter_all:           'All',
    filter_checked_in:    'Checked In',
    filter_not_checked:   'Not Checked',
    filter_all_dates:     'All Dates',
    search_bookings:      'Search by code, user, trip...',
    th_code:              'Code',
    th_user:              'User',
    th_trip_departure:    'Trip / Departure',
    th_checked:           'Checked',
    modal_new_booking:    'New Booking',
    modal_booking_sub:    'Select a trip and add passenger seats',
    label_trip:           'Trip Instance',
    label_available_seats:'Available Seats',
    label_pick_seat:      'Pick a seat to add...',
    btn_add_passenger:    'Add Passenger',
    btn_create_booking:   'Create Booking',
    label_passenger_name: 'Passenger Name',
    label_phone:          'Phone',
    label_status:         'Status',
    modal_edit_booking:   'Edit Booking',
    modal_passengers:     'Passengers',
    modal_cancel_title:   'Cancel Booking?',
    cancel_warn:          'You are about to cancel booking',
    cancel_warn2:         'The seats will be released.',
    no_available_seats:   'No available seats on this trip',
    no_passenger_details: 'No passenger details available.',
    checked_yes:          'Yes',
    checked_no:           'No',
    loading_seats:        'Loading seats...',
    select_trip:          'Select trip...',
    select_status:        'Select status...',
    status_reserved:      'Reserved',
    status_confirmed:     'Confirmed',
    status_cancelled:     'Cancelled',
    booking_code_label:   'Booking Code',

    // ── Trip Instances (My Trips) page ──────────────────
    page_my_trips:        'My Trips',
    kpi_total_trips:      'Total Trips',
    kpi_avail_seats:      'Available Seats',
    kpi_reserved_seats:   'Reserved Seats',
    search_trips:         'Search by route, bus, driver...',
    filter_all_schedules: 'All Schedules',
    filter_all_companies: 'All Companies',
    filter_all_dates_2:   'All Dates',
    th_route:             'Route',
    th_departure:         'Departure',
    th_arrival:           'Arrival',
    th_seats:             'Seats',
    th_bus_driver:        'Bus / Driver',
    th_details:           'Details',
    no_driver:            'No driver',
    departure_label:      'Departure',
    arrival_label:        'Arrival',
    seat_legend_avail:    'Available',
    seat_legend_resv:     'Reserved',
    reserved_seats_detail:'Reserved Seats Detail',
    seat_label:           'Seat',

    // ── Routes page ─────────────────────────────────────
    page_routes:          'Bus Routes',
    kpi_total_routes:     'Total Routes',
    kpi_offices_covered:  'Offices Covered',
    kpi_unique_cities:    'Unique Cities',
    search_routes:        'Search by city or office...',
    filter_all_offices:   'All Offices',
    btn_new_route_2:      'New Route',
    th_office:            'Office',
    from_label:           'Departure',
    to_label:             'Destination',
    modal_new_route:      'New Route',
    modal_route_sub:      'Define a new bus route between two cities',
    label_from_city:      'From City',
    label_to_city:        'To City',
    label_office:         'Office',
    select_office:        'Select office...',
    select_from:          'Select departure city...',
    select_to:            'Select destination city...',
    btn_create_route:     'Create Route',
    modal_edit_route:     'Edit Route',
    modal_delete_route:   'Delete Route?',
    route_delete_warn:    'You are about to permanently delete route',
    route_delete_warn2:   'All associated data will be lost.',

    // ── Trip Schedules page ──────────────────────────────
    page_schedules:       'Trip Schedules',
    kpi_total_schedules:  'Total Schedules',
    kpi_routes_covered:   'Routes Covered',
    kpi_buses_assigned:   'Buses Assigned',
    search_schedules:     'Search by route or bus...',
    filter_all_routes:    'All Routes',
    filter_all_days:      'All Days',
    btn_new_schedule_2:   'New Schedule',
    modal_new_schedule:   'New Trip Schedule',
    modal_schedule_sub:   'Set route, times, price and active days',
    label_route:          'Route',
    label_bus:            'Default Bus',
    label_departure_time: 'Departure Time',
    label_arrival_time:   'Arrival Time',
    label_price:          'Price',
    label_active_days:    'Active Days',
    select_route:         'Select route...',
    select_bus:           'Select bus...',
    btn_create_schedule:  'Create Schedule',
    modal_edit_schedule:  'Edit Schedule',
    modal_delete_schedule:'Delete Schedule?',

    // ── Employees page ───────────────────────────────────
    page_employees:       'Employee Management',
    kpi_total_employees:  'Total Employees',
    kpi_drivers:          'Drivers',
    kpi_managers:         'Managers',
    search_employees:     'Search by name, email, office...',
    filter_all_types:     'All Types',
    btn_new_employee_2:   'New Employee',

    // ── Shared empty / loading ───────────────────────────
    loading_generic:      'Loading...',
    no_results_title:     'No results found',
    no_results_desc:      'Try adjusting your search or filters.',
    card_view:            'Card view',
    list_view:            'List view',
  },

  ar: {
    // ── Brand ──────────────────────────────────────────
    brand_name:    'محطة الباص',
    brand_sub:     'بوابة الإدارة',

    // ── Sidebar section labels ──────────────────────────
    section_operations:   'العمليات',
    section_management:   'الإدارة',
    section_admin:        'الصلاحيات',

    // ── Nav items ───────────────────────────────────────
    nav_overview:         'نظرة عامة',
    nav_routes:           'المسارات',
    nav_trip_schedules:   'جداول الرحلات',
    nav_my_trips:         'رحلاتي',
    nav_bookings:         'الحجوزات',
    nav_payments:         'المدفوعات',
    nav_fleet:            'الأسطول',
    nav_company:          'الشركة',
    nav_bus_owners:       'ملاك الباصات',
    nav_bus_companies:    'شركات الباص',
    nav_offices:          'مكاتب الشركة',
    nav_employees:        'الموظفون',
    nav_customers:        'العملاء',
    nav_location:         'المواقع',
    nav_reports:          'التقارير',
    nav_roles:            'الأدوار والصلاحيات',
    nav_assign_roles:     'تعيين الأدوار',

    // ── Topbar ──────────────────────────────────────────
    search_placeholder:   'ابحث عن أي شيء...',
    admin_name:           'المدير',
    admin_role:           'مدير عام',

    // ── Toolbar shared ──────────────────────────────────
    btn_refresh:          'تحديث',
    btn_new_booking:      'حجز جديد',
    btn_new_schedule:     'جدول جديد',
    btn_new_route:        'مسار جديد',
    btn_new_employee:     'موظف جديد',
    btn_save:             'حفظ التغييرات',
    btn_cancel:           'إلغاء',
    btn_close:            'إغلاق',
    btn_edit:             'تعديل',
    btn_delete:           'حذف',
    btn_create:           'إنشاء',
    btn_yes_cancel:       'نعم، إلغاء',
    btn_keep:             'إبقاء الحجز',

    // ── Common table headers ─────────────────────────────
    th_id:          'الرقم',
    th_status:      'الحالة',
    th_actions:     'الإجراءات',
    th_created:     'تاريخ الإنشاء',
    th_date:        'التاريخ',
    th_price:       'السعر',

    // ── Bookings page ───────────────────────────────────
    page_bookings:        'الحجوزات',
    kpi_total_bookings:   'إجمالي الحجوزات',
    kpi_confirmed:        'مؤكد',
    kpi_cancelled:        'ملغى',
    kpi_showing:          'المعروض',
    filter_all_statuses:  'جميع الحالات',
    filter_confirmed:     'مؤكد',
    filter_reserved:      'محجوز',
    filter_cancelled:     'ملغى',
    filter_pending:       'قيد الانتظار',
    filter_all:           'الكل',
    filter_checked_in:    'تم التسجيل',
    filter_not_checked:   'لم يُسجَّل',
    filter_all_dates:     'جميع التواريخ',
    search_bookings:      'ابحث بالكود أو المستخدم أو الرحلة...',
    th_code:              'الكود',
    th_user:              'المستخدم',
    th_trip_departure:    'الرحلة / الموعد',
    th_checked:           'مُسجَّل',
    modal_new_booking:    'حجز جديد',
    modal_booking_sub:    'اختر رحلة وأضف المقاعد',
    label_trip:           'رحلة',
    label_available_seats:'المقاعد المتاحة',
    label_pick_seat:      'اختر مقعداً...',
    btn_add_passenger:    'إضافة راكب',
    btn_create_booking:   'إنشاء الحجز',
    label_passenger_name: 'اسم الراكب',
    label_phone:          'الهاتف',
    label_status:         'الحالة',
    modal_edit_booking:   'تعديل الحجز',
    modal_passengers:     'الركاب',
    modal_cancel_title:   'إلغاء الحجز؟',
    cancel_warn:          'أنت على وشك إلغاء الحجز',
    cancel_warn2:         'سيتم تحرير المقاعد.',
    no_available_seats:   'لا توجد مقاعد متاحة في هذه الرحلة',
    no_passenger_details: 'لا تتوفر بيانات الركاب.',
    checked_yes:          'نعم',
    checked_no:           'لا',
    loading_seats:        'جاري تحميل المقاعد...',
    select_trip:          'اختر رحلة...',
    select_status:        'اختر الحالة...',
    status_reserved:      'محجوز',
    status_confirmed:     'مؤكد',
    status_cancelled:     'ملغى',
    booking_code_label:   'كود الحجز',

    // ── Trip Instances (My Trips) page ──────────────────
    page_my_trips:        'رحلاتي',
    kpi_total_trips:      'إجمالي الرحلات',
    kpi_avail_seats:      'المقاعد المتاحة',
    kpi_reserved_seats:   'المقاعد المحجوزة',
    search_trips:         'ابحث بالمسار أو الباص أو السائق...',
    filter_all_schedules: 'جميع الجداول',
    filter_all_companies: 'جميع الشركات',
    filter_all_dates_2:   'جميع التواريخ',
    th_route:             'المسار',
    th_departure:         'الانطلاق',
    th_arrival:           'الوصول',
    th_seats:             'المقاعد',
    th_bus_driver:        'الباص / السائق',
    th_details:           'التفاصيل',
    no_driver:            'لا يوجد سائق',
    departure_label:      'الانطلاق',
    arrival_label:        'الوصول',
    seat_legend_avail:    'متاح',
    seat_legend_resv:     'محجوز',
    reserved_seats_detail:'تفاصيل المقاعد المحجوزة',
    seat_label:           'مقعد',

    // ── Routes page ─────────────────────────────────────
    page_routes:          'مسارات الباص',
    kpi_total_routes:     'إجمالي المسارات',
    kpi_offices_covered:  'المكاتب المشمولة',
    kpi_unique_cities:    'المدن الفريدة',
    search_routes:        'ابحث بالمدينة أو المكتب...',
    filter_all_offices:   'جميع المكاتب',
    btn_new_route_2:      'مسار جديد',
    th_office:            'المكتب',
    from_label:           'من',
    to_label:             'إلى',
    modal_new_route:      'مسار جديد',
    modal_route_sub:      'حدد مسار باص جديد بين مدينتين',
    label_from_city:      'مدينة الانطلاق',
    label_to_city:        'مدينة الوصول',
    label_office:         'المكتب',
    select_office:        'اختر مكتباً...',
    select_from:          'اختر مدينة الانطلاق...',
    select_to:            'اختر مدينة الوصول...',
    btn_create_route:     'إنشاء المسار',
    modal_edit_route:     'تعديل المسار',
    modal_delete_route:   'حذف المسار؟',
    route_delete_warn:    'أنت على وشك حذف المسار',
    route_delete_warn2:   'ستُفقد جميع البيانات المرتبطة.',

    // ── Trip Schedules page ──────────────────────────────
    page_schedules:       'جداول الرحلات',
    kpi_total_schedules:  'إجمالي الجداول',
    kpi_routes_covered:   'المسارات المشمولة',
    kpi_buses_assigned:   'الباصات المخصصة',
    search_schedules:     'ابحث بالمسار أو الباص...',
    filter_all_routes:    'جميع المسارات',
    filter_all_days:      'جميع الأيام',
    btn_new_schedule_2:   'جدول جديد',
    modal_new_schedule:   'جدول رحلة جديد',
    modal_schedule_sub:   'حدد المسار والأوقات والسعر وأيام التشغيل',
    label_route:          'المسار',
    label_bus:            'الباص الافتراضي',
    label_departure_time: 'وقت الانطلاق',
    label_arrival_time:   'وقت الوصول',
    label_price:          'السعر',
    label_active_days:    'أيام التشغيل',
    select_route:         'اختر مساراً...',
    select_bus:           'اختر باصاً...',
    btn_create_schedule:  'إنشاء الجدول',
    modal_edit_schedule:  'تعديل الجدول',
    modal_delete_schedule:'حذف الجدول؟',

    // ── Employees page ───────────────────────────────────
    page_employees:       'إدارة الموظفين',
    kpi_total_employees:  'إجمالي الموظفين',
    kpi_drivers:          'السائقون',
    kpi_managers:         'المدراء',
    search_employees:     'ابحث بالاسم أو البريد أو المكتب...',
    filter_all_types:     'جميع الأنواع',
    btn_new_employee_2:   'موظف جديد',

    // ── Shared empty / loading ───────────────────────────
    loading_generic:      'جاري التحميل...',
    no_results_title:     'لا توجد نتائج',
    no_results_desc:      'حاول تعديل البحث أو الفلاتر.',
    card_view:            'عرض البطاقات',
    list_view:            'عرض القائمة',
  }
};

// ================================================================
// CORE ENGINE
// ================================================================

const I18N = {
  current: 'en',

  init() {
    this.current = localStorage.getItem('bs_lang') || 'en';
    this.apply(this.current);
  },

  t(key) {
    return TRANSLATIONS[this.current]?.[key] ?? TRANSLATIONS['en']?.[key] ?? key;
  },

  apply(lang) {
    this.current = lang;
    localStorage.setItem('bs_lang', lang);
    const isAr = lang === 'ar';

    // ── Direction & font ──────────────────────────────
    document.documentElement.setAttribute('dir', isAr ? 'rtl' : 'ltr');
    document.documentElement.setAttribute('lang', lang);
    document.body.classList.toggle('rtl', isAr);

    // ── Update all [data-i18n] elements ───────────────
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const val = this.t(key);
      if (el.tagName === 'INPUT' && el.hasAttribute('placeholder')) {
        el.placeholder = val;
      } else {
        el.textContent = val;
      }
    });

    // ── Update all [data-i18n-placeholder] ────────────
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      el.placeholder = this.t(el.getAttribute('data-i18n-placeholder'));
    });

    // ── Update lang button appearance ─────────────────
    const btn = document.getElementById('langToggleBtn');
    if (btn) {
      btn.innerHTML = isAr
        ? '<i class="fas fa-globe"></i> EN'
        : '<i class="fas fa-globe"></i> AR';
      btn.title = isAr ? 'Switch to English' : 'التبديل إلى العربية';
    }

    // ── Dispatch event so child pages can react ────────
    document.dispatchEvent(new CustomEvent('langchange', { detail: { lang, isAr } }));
  },

  toggle() {
    this.apply(this.current === 'en' ? 'ar' : 'en');
  }
};

// Auto-init on DOM ready
document.addEventListener('DOMContentLoaded', () => I18N.init());