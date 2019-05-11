from users.admin import UserAdmin
from users.models import User
from django.contrib import admin
from django.http import JsonResponse, HttpResponse

class TenantAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("[**] Here")    
        # if get_host() ==
        print(request.get_host())

        path = request.path 
        print("PATH ", path)

        arr = request.get_host().split(".")
        if len(arr) == 3:
            # tenant
            if "/nse-admin/" in request.path:
                # return JsonResponse({
                #     "message": "You are not allowed to access this route",
                #     "status": 400
                # })
                html_text = "<center><br><img src='https://i.ytimg.com/vi/MfqeM1D2fnQ/maxresdefault.jpg' /></center>"

                return HttpResponse(html_text)


        # if request.get_host() == "tenant1.my-domain.com:9001":
        #     try:
        #         admin.site.register(User, UserAdmin)
        #         print(dir(UserAdmin))
        #         print("---- CAN VIEW ----")
        #     except admin.sites.NotRegistered:
        #         admin.site.register(User, UserAdmin)
        #         print("Registered")
        #     except admin.sites.AlreadyRegistered:
        #         admin.site.unregister(User)
        #         admin.site.register(User, UserAdmin)
        #         print("Unregistered then registered again")
        #     except:
        #         print("Pass")




        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("[**] Now, here")
        return response


# admin.site.register(User, UserAdmin)
# print(dir(UserAdmin))