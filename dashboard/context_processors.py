def permissions(request):
    return {
        "user_permissions": request.session.get("bs_permissions", [])
    }